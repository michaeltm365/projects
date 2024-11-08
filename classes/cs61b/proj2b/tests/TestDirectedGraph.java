import ngrams.DirectedGraph;
import org.junit.jupiter.api.Test;

import java.util.TreeSet;

import static com.google.common.truth.Truth.assertThat;

public class TestDirectedGraph {
    @Test
    public void simpleTest() {
        DirectedGraph<TreeSet<String>> graph = new DirectedGraph<>();
        TreeSet<String> setZero = new TreeSet<>();
        TreeSet<String> setOne = new TreeSet<>();
        TreeSet<String> setTwo = new TreeSet<>();
        setZero.add("Dog");
        setOne.add("Cat");
        setTwo.add("Mouse");

        graph.addVertex(setZero);
        graph.addVertex(setOne);
        graph.addVertex(setTwo);

        graph.addEdge(0, 1);
        graph.addEdge(0, 2);

        TreeSet<Integer> expected = new TreeSet<>();
        expected.add(1);
        expected.add(2);

        assertThat(graph.adj(0)).isEqualTo(expected);

        TreeSet<String> getExpected = new TreeSet<>();
        getExpected.add("Dog");
        assertThat(graph.getVertex(0)).isEqualTo(getExpected);
    }
}
