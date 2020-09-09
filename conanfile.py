from conans import ConanFile, CMake, tools
import os


class GladConan(ConanFile):
  name = "glad"
  version = "1.0.0"
  license = "MIT"
  url = "https://github.com/ck33122/glad"
  description = "conan glad package"
  settings = "os", "compiler", "build_type", "arch"
  generators = "cmake"
  exports_sources = "src%s*" % os.sep
  requires = ""

  def build(self):
    print("self.dir_bld(): %s" % self.dir_bld())
    print("self.dir_src(): %s" % self.dir_src())
    cmake = CMake(self)
    tools.mkdir(self.dir_bld())
    cmake.configure(source_folder=self.dir_src(), cache_build_folder=self.dir_bld())
    cmake.build(build_dir=self.dir_bld())

  def package(self):
    self.copy("*.h", src="%s%ssrc" % (self.dir_src(), os.sep), dst="include", keep_path=False)
    self.copy("*.dll", dst="bin", keep_path=False)
    self.copy("*.lib", dst="lib", keep_path=False)
    self.copy("*.so", dst="lib", keep_path=False)
    self.copy("*.so.*", dst="lib", keep_path=False)
    self.copy("*.dylib", dst="lib", keep_path=False)
    self.copy("*.a", dst="lib", keep_path=False)

  def package_info(self):
    self.cpp_info.includedirs = ['include']
    if self.settings.os == "Windows":
      self.cpp_info.libs = ["glad.lib"]
    elif self.settings.os == "Linux":
      self.cpp_info.libs = ["libglad.a"]
    else:
      self.output.error("unknown platform %s, need to fix conanfile.py" % self.settings.os)

  def dir_src(self):
    try:
      return self.src_full_path
    except:
      self.src_full_path = "%s%ssrc" % (self.source_folder, os.sep)
      return self.src_full_path

  def dir_bld(self):
    try:
      return self.build_full_path
    except:
      self.build_full_path = "%s%sbuild" % (self.dir_src(), os.sep)
      return self.build_full_path
