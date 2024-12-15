import 'package:ai_gen/vs_node_view/vs_node_view.dart';
import 'package:flutter/material.dart';

import 'helper/legend.dart';
import 'node_builder/node_builder.dart';

class VSNodeExample extends StatefulWidget {
  const VSNodeExample({super.key});

  @override
  State<VSNodeExample> createState() => _VSNodeExampleState();
}

class _VSNodeExampleState extends State<VSNodeExample> {
  Iterable<String>? results;

  VSNodeDataProvider nodeDataProvider = VSNodeDataProvider(
    nodeManager: VSNodeManager(nodeBuilders: NodeBuilder.nodeBuilders),
  );

  @override
  void initState() {
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: [
          InteractiveVSNodeView(
            width: 5000,
            height: 5000,
            nodeDataProvider: nodeDataProvider,
          ),
          const Positioned(
            bottom: 0,
            right: 0,
            child: Legend(),
          ),
          Positioned(
            top: 50,
            right: 10,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.end,
              children: [
                ElevatedButton(
                  onPressed: () async {
                    List<MapEntry<String, dynamic>> entries =
                        nodeDataProvider.nodeManager.getOutputNodes
                            .map(
                              (e) => e.evaluate(
                                  // onError: (_, __) => Future.delayed(Duration.zero, () {
                                  //   print("Error : ${_.toString()}");
                                  // }),
                                  ),
                            )
                            .toList();
                    print("entries: $entries");
                    for (var i = 0; i < entries.length; i++) {
                      var asyncOutput = await entries[i].value;
                      entries[i] = MapEntry(entries[i].key, asyncOutput);
                    }

                    results = entries.map((e) {
                      return "${e.key}: ${e.value}";
                    });
                    setState(() {});
                  },
                  child: const Text("Evaluate"),
                ),
                if (results != null)
                  ...results!.map(
                    (e) => Card(
                      child: Padding(
                        padding: const EdgeInsets.all(8.0),
                        child: Text(e),
                      ),
                    ),
                  ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
