from conans import ConanFile, CMake, tools

class ItkConan(ConanFile):
    name = "itk"
    version = "4.13.2"
    author = "Amir Kalali a.kalali@dkfz-heidelberg.de"
    homepage = "http://www.itk.org/"
    url = "https://github.com/akalali/conan-recipes/matchpoint"
    description = "Insight Segmentation and Registration Toolkit"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    short_paths = True

    _build_folder = "build"
    _source_folder = "ITK"

# PRIVATE FUNCTIONS
    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_EXAMPLES"] = "OFF"
        cmake.definitions["BUILD_SHARED_LIBS"] = self.options.shared
        cmake.definitions["BUILD_TESTING"] = "OFF"
        cmake.definitions["BUILD_DOCUMENTATION"] = "OFF"

        cmake.definitions["Module_IsotropicWavelets"] = "ON"
        cmake.definitions["Module_ITKOpenJPEG"] = "ON"
        cmake.definitions["Module_ITKReview"] = "ON"

        cmake.definitions["ITK_USE_SYSTEM_GDCM"] = "OFF" # switch to ON
        cmake.definitions["ITK_USE_SYSTEM_HDF5"] = "OFF" # switch to ON

        cmake.configure(source_folder = self._source_folder, build_folder = self._build_folder)
        return cmake

# PUBLIC FUNCTIONS USED BY CONAN
    def source(self):
        self.run("git clone --depth 1 --branch v4.13.2 https://github.com/InsightSoftwareConsortium/ITK.git")

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.builddirs = ['lib/cmake/ITK-4.13']
        self.cpp_info.includedirs.append('include/ITK-4.13')
        self.cpp_info.libs = tools.collect_libs(self)
