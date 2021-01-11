# CMakeList.txt : Top-level CMake project file, do global configuration
# and include sub-projects here.
#
cmake_minimum_required (VERSION 3.8)

project ("ConanWSL")

execute_process(COMMAND python conan_init.py WORKING_DIRECTORY "${CMAKE_SOURCE_DIR}")

# Include sub-projects.
add_subdirectory ("src1")
