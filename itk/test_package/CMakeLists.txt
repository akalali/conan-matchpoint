cmake_minimum_required(VERSION 2.8.12)
project(test_package CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(${PROJECT_NAME} test_package.cpp)

target_include_directories(${PROJECT_NAME} PRIVATE ${CONAN_INCLUDE_DIRS_ITK})
target_link_libraries(${PROJECT_NAME} ${CONAN_LIBS})
