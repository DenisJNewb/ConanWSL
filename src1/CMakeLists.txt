cmake_minimum_required (VERSION 3.8)

set(CXX_STANDARD 20)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
CONAN_BASIC_SETUP()

add_executable (program "main.cpp")
target_link_libraries(program ${CONAN_LIBS})

install(TARGETS program)
