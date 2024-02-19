#include <iostream>
#include <string>
#include <ctype.h>

int main() {
    std::string keyword, message;
    std::getline(std::cin, keyword);
    std::getline(std::cin, message);

    for (int i = 0; i < message.length(); i++) {
        if (!isalpha(message[i])) {
            message.erase(i--, 1);
        } else {
            int shift = (keyword[i % keyword.length()] - 65);
            if (message[i] + shift > 90) {
                shift -= 26;
            }

            message[i] += shift;
        }
    }

    std::cout << message;

    return 0; 
}