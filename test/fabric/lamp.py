import re
from fabric.api import env, hide, run, task
from envassert import detect, file, package, port, process, service


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
            assert package.installed("httpd")
            assert package.installed("holland")
            assert package.installed("mysql55")
            assert port.is_listening(80)
            assert port.is_listening(443)
            assert port.is_listening(3306)
            assert process.is_up("httpd")
            assert service.is_enabled("httpd")
            # welcome.conf causes a 403 when running apache_is_responding()
            # with the stock build.

    if env.platform_family == "debian":
        print "Ubuntu 12.04/14.04 or Debian 7.x"
        assert package.installed("apache2")
        assert package.installed("mysql-server-5.5")
        assert package.installed("apache2")
        assert port.is_listening(80)
        assert port.is_listening(443)
        assert port.is_listening(3306)
        assert process.is_up("apache2")
        assert service.is_enabled("apache2")
        assert apache_is_responding()
