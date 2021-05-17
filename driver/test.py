import hashlib
import os
import platform
import re
import tempfile
import sys
import zipfile

from urllib import request


plat = platform.platform().lower()
chromedriver_version = '90.0.4430.24'
build_dir = os.path.abspath(os.getcwd())


"""Downloads and unzips the requested chromedriver executable."""
CHROMEDRIVER_URL_TEMPLATE = (
    'http://chromedriver.storage.googleapis.com/{version}/chromedriver_{os_}'
    '{architecture}.zip'
)
def _download(zip_path):
    plat = platform.platform().lower()
    if plat.startswith('darwin'):
        os_ = 'mac'
        # Only 64 bit architecture is available for mac since version 2.23
        architecture = 64 if float(chromedriver_version) >= 2.23 else 32
    elif plat.startswith('linux'):
        os_ = 'linux'
        architecture = platform.architecture()[0][:-3]
    elif plat.startswith('win'):
        os_ = 'win'
        architecture = 32
    else:
        raise Exception('Unsupported platform: {0}'.format(plat))

    url = CHROMEDRIVER_URL_TEMPLATE.format(version=chromedriver_version,
                                            os_=os_,
                                            architecture=architecture)

    download_report_template = ("\t - downloading from '{0}' to '{1}'"
                                .format(url, zip_path))

    def reporthoook(x, y, z):
        global download_ok

        percent_downloaded = '{0:.0%}'.format((x * y) / float(z))
        sys.stdout.write('\r')
        sys.stdout.write("{0} [{1}]".format(download_report_template,
                                            percent_downloaded))
        download_ok =  percent_downloaded == '100%'
        if download_ok:
            sys.stdout.write(' OK')
        sys.stdout.flush()

    request.urlretrieve(url, zip_path, reporthoook)

    print('')
    if not download_ok:
        print('\t - download failed!')

    

def _unzip(zip_path):
    zf = zipfile.ZipFile(zip_path)
    print("\t - extracting '{0}' to '{1}'."
            .format(zip_path, build_dir))
    zf.extractall(build_dir)



def run():

    validate = False
    
    file_name = 'chromedriver_{0}.zip'.format(chromedriver_version)
    zip_path = os.path.join(tempfile.gettempdir(), file_name)

    if validate:
        if os.path.exists(zip_path):
            print("\t - requested file '{0}' found at '{1}'."
                    .format(file_name, zip_path))
        else:
            _download(zip_path)
    else:
        _download(zip_path)

    _unzip(zip_path)
    
run()

