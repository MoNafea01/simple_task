import 'package:ai_gen/vs_node_view/vs_node_view.dart';
import 'package:flutter/material.dart';

import 'helper/constants.dart';
import 'helper/legend.dart';

class VSNodeExample extends StatefulWidget {
  const VSNodeExample({super.key});

  @override
  State<VSNodeExample> createState() => _VSNodeExampleState();
}

class _VSNodeExampleState extends State<VSNodeExample> {
  Iterable<String>? results;

  VSNodeDataProvider nodeDataProvider = VSNodeDataProvider(
    nodeManager: VSNodeManager(nodeBuilders: VSHelper.nodeBuilders),
  );

  @override
  void initState() {
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Stack(
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
          top: 0,
          right: 0,
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.end,
            children: [
              ElevatedButton(
                onPressed: () {
                  print(
                      "nodeDataProvider.nodeManager.getOutputNodes: ${nodeDataProvider.nodeManager.getOutputNodes}");
                  Iterable<MapEntry<String, dynamic>> entries =
                      nodeDataProvider.nodeManager.getOutputNodes.map(
                    (e) => e.evaluate(
                      onError: (_, __) => Future.delayed(Duration.zero, () {
                        print(_.toString());
                        ScaffoldMessenger.of(context).showSnackBar(
                          const SnackBar(
                            backgroundColor: Colors.deepOrange,
                            content: Text('An error occured'),
                          ),
                        );
                      }),
                    ),
                  );

                  results = entries.map((e) => "${e.key}: ${e.value}");

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
    );
  }
}
