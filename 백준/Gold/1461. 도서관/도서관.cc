/*
* 22/08/14
* Oh Jin Young
*/
#include <iostream>
#include <algorithm>

using namespace std;

int N, M, dist;
int book[50];

bool cmp(int a, int b) {
	return a > b;
}

bool caculate() {
	int i, idx = 0;
	for (i = 1; i < N; i++) {
		if (book[idx] * book[i] < 0) {
			break;
		}
	}
	idx = i;

	i = 0;
	while (i + M <= idx) {
		dist += abs(book[i]) * 2;
		i += M;
	}
	if (i != idx) dist += abs(book[i]) * 2;
	if(idx!=N)return true;
	return false;
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	cin >> N >> M;

	for (int i = 0; i < N; i++) cin >> book[i];
	
	sort(book, book + N);
	if (caculate()) {
		sort(book, book + N, cmp);
		caculate();
	}
	else {
		int dist2 = dist;
		dist = 0;
		sort(book, book + N, cmp);
		caculate();
		dist = max(dist, dist2);
	}
	
	cout << dist - max(abs(book[N - 1]), book[0]);
	return 0;
}
