cmake_minimum_required(VERSION 3.10 FATAL_ERROR)
project(glad C)

add_library(glad STATIC ${CMAKE_CURRENT_SOURCE_DIR}/src/glad.c)
target_link_libraries(glad PUBLIC ${CMAKE_DL_LIBS})
target_include_directories(glad PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)
