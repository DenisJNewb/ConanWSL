#include <iostream>
#include <string>

#include <fmt/core.h>

using namespace std;

int main()
{
	string test = fmt::format("Format this {} string", "cool");
	printf("%s\n", test.c_str());
	cin.get();
}
