from distutils.core import setup, Extension
import os
import sys

# set the fortran runtime lib. appropriately.

platform = sys.platform[:5]
if (platform == 'linux'):
      fortranlib = ['g2c']
      fflags = '-O -c -fPIC'
      cflags = '-O -c -fPIC'
      ldflags = ''
      cc = 'gcc'
      fc = 'g77'
elif (platform == 'cygwi'):
      fortranlib == ['g2c']
      fflags = '-O -c'
      cflags = '-O -c'
      ldflags = ''
      cc = 'gcc'
      fc = 'g77'
elif (platform == 'sunos'):
      fortranlib = ['F77', 'M77', 'sunmath']
      fflags = '-O -c -KPIC'
      cflags = '-O -c -KPIC'
      ldflags = ''
      cc = 'cc'
      fc = 'f77'
elif (platform == 'darwi'):
      fortranlib = ['f2c']
      fflags = '-O -c -fno-common'
      cflags = '-O -c -no-cpp-precompile -fno-common'
      ldflags = '-L/sw/lib'
      cc = 'cc'
      fc = 'f77'

flib = ' '.join(map(lambda a:'-l%s'%a, fortranlib))
macros = '"CC=%s" "FC=%s" '%(cc, fc)
macros = macros + '"FORTRANLIB=%s" '%flib
macros = macros + '"CFLAGS=%s" '%cflags
macros = macros + '"FFLAGS=%s" '%fflags 
macros = macros + '"LDFLAGS=%s" '%ldflags 

os.system("make lib %s"%macros)
if (sys.argv[1] == 'sfac'):
      os.system("make sfac %s"%macros)
      os.system("make install")
else:
      libs = ["fac", "quadpack", "lapack", "blas", "coul",
              "toms", "mpfun", "minpack", "ionis", "m"] + fortranlib
      libdir = ["faclib", "coul", "toms", "mpfun", "minpack",
                "quadpack", "lapack", "blas", "ionis"]
      incdir = ["faclib"]
    
      setup(name = "FAC",
            version = "0.7.2",
            package_dir = {'pfac': 'python'},
            py_modules = ['pfac.const', 'pfac.config', 
                          'pfac.atom', 'pfac.spm'],
            ext_modules = [Extension("pfac.fac",
                                     ["python/fac.c"],
                                     include_dirs = incdir,
                                     library_dirs = libdir,
                                     libraries = libs),
                           Extension("pfac.crm",
                                     ["python/pcrm.c"],
                                     include_dirs = incdir,
                                     library_dirs = libdir,
                                     libraries = libs)
                           ])
