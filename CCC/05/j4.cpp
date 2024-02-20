#include <iostream>
#include <set>
#include <vector>

std::vector<int> operator+(std::vector<int> v1, std::vector<int> v2) {
    v1[0] += v2[0];
    v1[1] += v2[1];

    return v1;
}

std::set<std::vector<int>> walls(int w1, int h1, int w2, int h2) {
    std::set<std::vector<int>> res = {};

    for (int x = 1; x <= w1; x++) {
        for (int y = 1; y <= h1; y++) {
            if ((x <= w2 && (y <= h2 || y > h1 - h2)) || (x > w1 - w2 && (y <= h2 || y > h1 - h2))) {
                res.insert({x, y});
            }
        }
    }
    
    return res;
}

int numOfAdj(std::vector<int> pos, std::set<std::vector<int>> blocked, int w1, int h1) {
    std::vector<std::vector<int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    int res = 0;

    for (std::vector<int> direction : directions) {
        std::vector<int> newPos = pos + direction;
        if (newPos[0] >= 1 && newPos[0] <= w1 && newPos[1] >= 1 && newPos[1] <= h1 && !blocked.count(newPos)) {
            res += 1;
        }
    }

    return res;
}

bool outOfBounds(int w, int h, std::vector<int> pos) {
    return pos[0] < 1 || pos[0] > w || pos[1] < 1 || pos[1] > h;
}

int main() {
    int w1, h1, w2, h2, steps;
    std::cin >> w1;
    std::cin >> h1;
    std::cin >> w2;
    std::cin >> h2;
    std::cin >> steps;
    
    std::vector<int> pos = {w2 + 1, 1};
    std::set<std::vector<int>> blocked = walls(w1, h1, w2, h2);
    std::vector<std::vector<int>> directions = {{1, 0}, {0, 1}, {1, 0}, {0, 1}, {-1, 0}, {0, 1}, {-1, 0}, {0, -1}, {-1, 0}, {0, -1}, {1, 0}, {0, -1}};

    int curDir = 0;

    for (int i = 0; i <= steps; i++) {
        std::cout << pos[0] << "," << pos[1] << " ";

        if (blocked.count(pos + directions[curDir]) || numOfAdj(pos, blocked, w1, h1) == 4 || outOfBounds(w1, h1, pos + directions[curDir])) {
            curDir = (curDir + 1) % 12;
        }
        pos = pos + directions[curDir];
    }

    return 0;
}