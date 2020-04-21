cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(example example.cpp)

target_include_directories(example PRIVATE ${CONAN_INCLUDE_DIRS_ITK})
target_link_libraries(example ${CONAN_LIBS} ${CMAKE_DL_LIBS})
