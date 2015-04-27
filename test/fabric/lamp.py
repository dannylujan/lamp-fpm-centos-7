from fabric.api import env, hide, run, task
from envassert import detect, file, package, port, process, service
from hot.utils.test import get_artifacts


def phpmyadmin_is_responding():
    assert file.exists('/root/.phpmyadminpass'), ("/root/.phpmyadminpass" +
                                                  " not found")
    credentials = ''
    with hide('running', 'stdout'):
        credentials = run("cat /root/.phpmyadminpass")
    htuser = credentials.split(' ')[0]
    htpass = credentials.split(' ')[1]
    with hide('running', 'stdout'):
        phpmyadmin = run("curl -IL http://localhost/phpmyadmin -u '" +
                         htuser + ":" + htpass + "'")
        return True


def holland_is_running():
    with hide('running', 'stdout'):
        holland = run("holland bk")
        return True


def apache_is_responding():
    with hide('running', 'stdout'):
        homepage = run("wget --quiet --output-document - http://localhost/")
        return True


@task
def check():
    env.platform_family = detect.detect()
    release = run("/usr/bin/lsb_release -r | awk {'print $2'}")

    if env.platform_family == "rhel":
        if float(release) < 7:
            print "RHEL/Cent 6.x"
            assert package.installed("httpd"), "httpd not installed"
            assert package.installed("holland"), "holland is not installed"
            assert package.installed("mysql55"), "mysql55 is not insalled"
            assert process.is_up("httpd"), "process httpd not running"
            assert service.is_enabled("httpd"), "httpd not enabled"
            # welcome.conf causes a 403 when running apache_is_responding()
            # with the stock build.

    if env.platform_family == "debian":
        print "Ubuntu 12.04/14.04 or Debian 7.x/8.x"
        assert package.installed("apache2"), "apache2 is not installed"
        assert package.installed("mysql-server-5.5"), ("mysql-server-5.5 not" +
                                                       " installed")
        assert process.is_up("apache2"), "apache2 is not running"
        assert service.is_enabled("apache2"), "apache2 is not enabled"
        assert apache_is_responding(), "apache2 is not responding"

    assert port.is_listening(80), "port 80 not listening"
    assert port.is_listening(443), "port 443 not listening"
    assert port.is_listening(3306), "port 3306 not listening"
    assert phpmyadmin_is_responding(), "phpmyadmin is not responding"
    assert holland_is_running(), "holland cannot run"


@task
def artifacts():
    env.platform_family = detect.detect()
    get_artifacts()
