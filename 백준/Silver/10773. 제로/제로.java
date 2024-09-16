import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main
{
    // tip: arguments are passed via the field below this editor
    static ArrayList<Integer> moneis = new ArrayList<>();
    static Integer len = 0;

    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        Integer K = Integer.parseInt(st.nextToken());
        int ans = 0;

        for(int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            if(n != 0) {
                moneis.add(n);
                len++;
            }
            else {
                moneis.remove(len-1);
                len--;
            }
        }

        for(int i = 0; i < len; i++) {
            ans += moneis.get(i);
        }
        bw.write(ans + "\n");
        bw.flush();
        bw.close();
        br.close();
    }
}
