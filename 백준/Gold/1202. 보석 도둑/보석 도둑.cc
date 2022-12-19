#include <iostream>
#include <queue>
#include <algorithm>
#include <set>

using namespace std;

int total_dia, total_bag;
long long ans;
vector<pair<int, int>> dia;
vector<int> bag;
priority_queue <int> PQ_dia;

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	cin >> total_dia >> total_bag;


	for (int i = 0; i < total_dia; i++) {
		int w, v;
		cin >> w >> v;
		dia.push_back(make_pair(w, v));
	}

	for (int i = 0; i < total_bag; i++) {
		int w;
		cin >> w;
		bag.push_back(w);
	}

	sort(dia.begin(), dia.end());
	sort(bag.begin(), bag.end());
	int current = 0;
	for (int i = 0; i < total_bag; i++) {
		while (current < total_dia && dia[current].first <= bag[i]) {
			PQ_dia.push(dia[current].second);
			current++;
		}
		if (!PQ_dia.empty()) {
			ans += PQ_dia.top();
			PQ_dia.pop();
		}
	}
	cout << ans;

	return 0;
}