#include <iostream>
#include <string>
#include <unordered_map>

int main() {
    std::unordered_map<int, std::string> nums {
        {1, "\n      *\n      *\n      *\n\n      *\n      *\n      *\n\n"},
        {2, " * * *\n      *\n      *\n      *\n * * *\n*\n*\n*\n * * *\n"},
        {3, " * * *\n      *\n      *\n      *\n * * *\n      *\n      *\n      *\n * * *\n"},
        {4, "\n*     *\n*     *\n*     *\n * * *\n      *\n      *\n      *\n\n"},
        {5, " * * *\n*\n*\n*\n * * *\n      *\n      *\n      *\n * * *\n"},
        {6, " * * *\n*\n*\n*\n * * *\n*     *\n*     *\n*     *\n * * *\n"},
        {7, " * * *\n      *\n      *\n      *\n\n      *\n      *\n      *\n\n"},
        {8, " * * *\n*     *\n*     *\n*     *\n * * *\n*     *\n*     *\n*     *\n * * *\n"},
        {9, " * * *\n*     *\n*     *\n*     *\n * * *\n      *\n      *\n      *\n * * *\n"},
        {0, " * * *\n*     *\n*     *\n*     *\n\n*     *\n*     *\n*     *\n * * *\n"}
    };
    
    int n;

    std::cin >> n;
    std::cout << nums[n];

}