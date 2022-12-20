#include <iostream>
#include <vector>

using namespace std;

int N;
bool visit[100001];
int parent[100001];
vector<vector<int>> tree;

void dfs(int n) {
	for (int num : tree[n]) {
		if (!visit[num]) {
			parent[num] = n;
			visit[num] = true;
			dfs(num);
		}
	}
}

int main() {
	cin >> N;

	for (int i = 0; i <= N; i++) {
		vector<int> v;
		tree.push_back(v);
	}

	for (int i = 1; i < N; i++) {
		int a, b;
		cin >> a >> b;

		tree[b].push_back(a);
		tree[a].push_back(b);
	}
	visit[1] = true;
	dfs(1);
	for (int i = 2; i <= N; i++) cout << parent[i]<< "\n";

	return 0;
}