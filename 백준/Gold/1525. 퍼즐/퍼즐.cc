#include <iostream>
#include <map>
#include <queue>

using namespace std;

map<int, bool> m;

int swap(int zero_i, int swap_i, int puzz[10]) {
	int puz[10];
	for (int i = 1; i <= 9; i++) puz[i] = puzz[i];
	puz[zero_i] =  puz[swap_i];
	puz[swap_i] = 0;

	int swaped = 0;
	int idx = 1;
	for (int i = 100000000; i >= 1; i /= 10) {
		swaped += (puz[idx++] * i);
	}
	return swaped;
}

void bfs(int p) {
	queue<pair<int,int>> q;

	q.push(make_pair(p, 0));

	while (!q.empty()) {

		int num = q.front().first;
		int cnt = q.front().second;

		if (num == 123456780) {
			cout << cnt;
			exit(0);
		}
		m.insert({ num, true });

		q.pop();

		int puzzle[10], index = 1, zero_index;
		for (int i = 100000000; index <= 9; i /= 10) {
			puzzle[index] = num / i;
			if (puzzle[index] == 0) zero_index = index;
			num = num % i;
			index++;
		}

		int pz;
		zero_index--;
		if (zero_index + 3 <= 8) {
			pz = swap(zero_index + 1, zero_index + 4, puzzle);
			if (m.find(pz) != m.end());
			else {
				m.insert({ pz,true });
				q.push(make_pair(pz, cnt + 1));
			}
		}
		if (zero_index / 3 == (zero_index + 1) / 3) {
			pz = swap(zero_index + 1, zero_index + 2, puzzle);
			if (m.find(pz) != m.end());
			else {
				m.insert({ pz,true });
				q.push(make_pair(pz, cnt + 1));
			}
		}
		if (zero_index - 3 >= 0) {
			pz = swap(zero_index + 1, zero_index - 2, puzzle);
			if (m.find(pz) != m.end());
			else {
				m.insert({ pz,true });
				q.push(make_pair(pz, cnt + 1));
			}
		}
		if (zero_index / 3 == (zero_index - 1) / 3 && zero_index != 0) {
			pz = swap(zero_index + 1, zero_index, puzzle);
			if (m.find(pz) != m.end());
			else {
				m.insert({ pz,true });
				q.push(make_pair(pz, cnt + 1));
			}
		}
	}

	cout << -1;

}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int n, m = 0;
	for (int i = 100000000; i >= 1; i /= 10) {
		cin >> n;
		m += (n * i);
	}
	
	bfs(m);
	

	return 0;
}