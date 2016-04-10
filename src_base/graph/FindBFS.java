package graph;

import java.util.HashSet;
import java.util.LinkedList;
import java.util.Set;

/**
 * 图的广度优先遍历
 */
public class FindBFS {


    public int find(Node start, Node end) {
        Set<Node> visited = new HashSet<>();

        //list
        LinkedList<Node> list = new LinkedList<>();

        list.addLast(start);

        int routeCount = 0;
        while (!list.isEmpty()) {
            routeCount++;
            Node node = list.removeFirst();

            for (Node neighbour : node.neighbours) {
                if (neighbour == end) {
                    return routeCount;
                }

                if (!visited.contains(neighbour)) {
                    visited.add(neighbour);
                }

                list.addLast(neighbour);
            }
        }
        return -1;
    }

}
