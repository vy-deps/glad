cmake_minimum_required(VERSION 3.10 FATAL_ERROR)
project(glad C)

add_library(glad STATIC ${CMAKE_CURRENT_SOURCE_DIR}/src/glad.c)
target_include_directories(glad PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)

if(UNIX AND NOT ANDROID_APP_PLATFORM AND NOT APPLE)
  target_compile_options(glad PRIVATE -fPIC)
endif()
