#include <iostream>
#include <string>
#include <map>

std::map<char, int> getCounts(std::string s) {
    std::map<char, int> counts = {};
    for (char c : s) {
        if (c == ' ') {
            continue;
        }

        if (counts.count(c)) {
            counts[c] += 1;
        } else {
            counts[c] = 1;
        }
    }

    return counts;
}

int main() {
    std::string s1, s2;
    std::getline(std::cin, s1);
    std::getline(std::cin, s2);

    if (getCounts(s1) == getCounts(s2)) {
        std::cout << "Is an anagram.";
    } else {
        std::cout << "Is not an anagram.";
    }
    
    return 0;
}