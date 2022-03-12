cmake_minimum_required(VERSION 3.10)

project(EXAMPLE)

set(EXAMPLE_VERSION_MAJOR 0)
set(EXAMPLE_VERSION_MINOR 1)

set(CMAKE_MODULE_PATH ${EXAMPLE_SOURCE_DIR}/cmake)

set(EXAMPLE_DIR "${CMAKE_BINARY_DIR}")

include(TranslationUtils)

if(UNIX)
  include(GNUInstallDirs)
else()
  if (WIN32)
    set(${CMAKE_INSTALL_LIBDIR} "lib")
    set(${CMAKE_INSTALL_DATADIR} "share")
    set(${CMAKE_INSTALL_INCLUDEDIR} "include")
    set(${CMAKE_INSTALL_BINDIR} "bin")
    message(STATUS "Setting installation destination on Windows to: ${CMAKE_INSTALL_PREFIX}")
  else()
    message(FATAL_ERROR "System not UNIX nor WIN32 - not implemented yet")
  endif()
endif()

# export the EXAMPLE package
export(PACKAGE EXAMPLE)

option(EXAMPLE_EXAMPLE_TESTS "Build the example tests." OFF)

add_subdirectory(src)

enable_testing()
add_subdirectory(tests)
