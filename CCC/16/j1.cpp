#include <iostream>
#include <vector>

int main() {
    std::vector<char> score {};
    for (int i = 0; i < 6; i++) {
        char temp;
        std::cin >> temp;
        score.push_back(temp);
    }

    int count = 0;
    for (char c : score) {
        if (c == 'W') {
            count++;
        }
    }

    if (count == 0) {
        std::cout << -1;
    } else if (count >= 5) {
        std::cout << 1;
    } else if (count >= 3) {
        std::cout << 2;
    } else {
        std::cout << 3;
    }

    return 0;
}