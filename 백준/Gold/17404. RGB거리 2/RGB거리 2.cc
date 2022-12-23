#include <iostream>
#include <algorithm>
using namespace std;

int house[3], N;
int house_current[3];
int ans;
int weight1[1001][1001];
int weight2[1001][1001];
int weight3[1001][1001];

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	
	cin >> N;
	for (int i = 1; i <= N; i++) {
		int r, g, b;
		cin >> r >> g >> b;
		weight1[0][i] = r; weight1[1][i] = g; weight1[2][i] = b;
		weight2[0][i] = r; weight2[1][i] = g; weight2[2][i] = b;
		weight3[0][i] = r; weight3[1][i] = g; weight3[2][i] = b;
	}

	weight1[1][1] = 9999; weight1[2][1] = 9999;
	weight2[0][1] = 9999; weight2[2][1] = 9999;
	weight3[0][1] = 9999; weight3[1][1] = 9999;


	for (int j = 2; j <= N; j++) for (int i = 0; i < 3; i++) weight1[i][j] = weight1[i][j] + min(weight1[(i + 1) % 3][j - 1], weight1[(i + 2) % 3][j - 1]);
	ans = min(weight1[1][N], weight1[2][N]);

	for (int j = 2; j <= N; j++) for (int i = 0; i < 3; i++) weight2[i][j] = weight2[i][j] + min(weight2[(i + 1) % 3][j - 1], weight2[(i + 2) % 3][j - 1]);
	ans = min(ans, min(weight2[0][N], weight2[2][N]));

	for (int j = 2; j <= N; j++) for (int i = 0; i < 3; i++) weight3[i][j] = weight3[i][j] + min(weight3[(i + 1) % 3][j - 1], weight3[(i + 2) % 3][j - 1]);
	ans = min(ans, min(weight3[0][N], weight3[1][N]));


	cout << ans << "\n";
	
	return 0;
}