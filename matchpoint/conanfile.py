import os

from conans import ConanFile, CMake, tools

class MatchpointConan(ConanFile):
    name = "matchpoint"
    version = "0.1"
    author = "Amir Kalali a.kalali@dkfz-heidelberg.de"
    url = "https://github.com/akalali/conan-recipes/matchpoint"
    description = "MatchPoint is a translational image registration framework written in C++. " \
                  "It offers a standardized interface to utilize several registration algorithm resources " \
                  "(like ITK, plastimatch, elastix) easily in a host application."
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    requires = "itk/4.13.2"

    _requirement_options = {"itk:shared": False}
    default_options.update(_requirement_options)

    _build_folder = "build"
    _source_folder = "MatchPoint"

    def source(self):
        self.run("git clone --depth 1 https://github.com/MIC-DKFZ/MatchPoint.git")

    def build(self):
        itk_rootpath = self.deps_cpp_info["itk"].rootpath
        itk_libpath = os.path.join(itk_rootpath, "lib", "cmake", "ITK-4.13")

        cmake = CMake(self)
        cmake.definitions["BUILD_SHARED_LIBS"] = self.options.shared
        cmake.definitions["BUILD_TESTING"] = "OFF"
        cmake.definitions["CMAKE_PREFIX_PATH"] = itk_libpath
        cmake.configure(source_folder = self._source_folder, build_folder = self._build_folder)
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="MatchPoint")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)