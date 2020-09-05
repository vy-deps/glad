#include "glad/glad.h"
#include "stdio.h"

int main()
{
  int r = gladLoadGL();
  fprintf(stderr, "gladLoadGL() = %d\n", r);
  fprintf(stderr, "major: %d\n", GLVersion.major);
  fprintf(stderr, "minor: %d\n", GLVersion.minor);
  return 0;
}
