package graph;

import java.util.HashSet;
import java.util.LinkedList;
import java.util.Set;

/**
 * 深度优先遍历
 */
public class FindDFS {

    public int find(Node start, Node end) {
        Set<Node> visited = new HashSet<>();

        //栈
        LinkedList<Node> list = new LinkedList<>();
        list.push(start);

        int routeCount = 0;
        while (!list.isEmpty()) {
            Node node = list.pop();

            routeCount++;

            for (Node neighbour : node.neighbours) {
                if (neighbour == end) {
                    return routeCount;
                }

                if (!visited.contains(neighbour)) {
                    visited.add(neighbour);
                }

                list.push(neighbour);
            }
        }
        return -1;
    }
}
