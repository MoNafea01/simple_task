import 'package:ai_gen/dmy_node_trys/my_node_red/src/nodes.dart';
import 'package:flutter/material.dart';

import 'my_node_grid.dart';
import 'my_node_red/node_editor.dart';

class MyNodeEditor extends StatefulWidget {
  const MyNodeEditor({super.key});

  @override
  State<MyNodeEditor> createState() => _MyNodeEditorState();
}

class _MyNodeEditorState extends State<MyNodeEditor> {
  NodesManager nodesManager = NodesManager();

  final NodeEditorController _controller = NodeEditorController();
  final FocusNode _focusNode = FocusNode();

  @override
  void initState() {
    super.initState();
  }

  @override
  void dispose() {
    _focusNode.dispose();
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("data"),
      ),
      body: MyNodeGrid(focusNode: _focusNode, controller: _controller),
      floatingActionButton: _fab(),
    );
  }

  FloatingActionButton _fab() {
    return FloatingActionButton(
      onPressed: () {
        // Add new node at random position
        final nodeNumber = _controller.nodes.length + 1;
        final randomX = 100.0 + (nodeNumber * 50);
        final randomY = 100.0 + (nodeNumber * 50);

        ContainerNodeWidget _testBlock = _trainTestBlock('Node $nodeNumber');

        // nodesManager.addNode(_testBlock, NodePosition.afterLast);
        // _controller.nodesManager.nodes;
        // _controller.addNode(
        //   _testBlock,
        //   NodePosition.centerScreen,
        // );
        for (var port in _controller.nodesManager.nodes.values
            .toList()[0]
            .properties
            .values
            .toList()) {
          print(port);
        }
        print(_controller.nodesManager.nodes.values.toList()[0].properties);
        print(_controller.nodesManager.nodes.values.toList()[0].name);
      },
      child: const Icon(Icons.add),
    );
  }

  ContainerNodeWidget _trainTestBlock(String name) {
    return ContainerNodeWidget(
      name: name,
      typeName: 'train_test',
      backgroundColor: Colors.green.shade800,
      radius: 100,
      width: 200,
      contentPadding: const EdgeInsets.all(4),
      selectedBorder: Border.all(color: Colors.white),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Column(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              InPortWidget(
                name: 'PortIn1',
                onConnect: (String name, String port) {
                  this._controller.nodes.values;
                  print("connected");
                  print("name: $name -- port : $port");
                  return true;
                },
                icon: const Icon(
                  Icons.circle_outlined,
                  color: Colors.yellowAccent,
                  size: 20,
                ),
                iconConnected: const Icon(
                  Icons.circle,
                  color: Colors.yellowAccent,
                  size: 20,
                ),
                multiConnections: false,
                connectionTheme:
                    ConnectionTheme(color: Colors.yellowAccent, strokeWidth: 2),
              ),
            ],
          ),
          const Icon(Icons.safety_divider),
          OutPortWidget(
            name: 'PortOut1',
            icon: Transform.flip(
              flipX: true,
              child: const Icon(
                Icons.arrow_back,
                color: Colors.blue,
                size: 24,
              ),
            ),
            iconConnected: const Icon(
              Icons.pause_circle,
              color: Colors.deepOrange,
              size: 24,
            ),
            multiConnections: false,
            connectionTheme:
                ConnectionTheme(color: Colors.deepOrange, strokeWidth: 2),
          ),
        ],
      ),
    );
  }

  ContainerNodeWidget _printBlock(String name) {
    return ContainerNodeWidget(
      name: name,
      typeName: 'print_block',
      backgroundColor: Colors.green.shade800,
      radius: 100,
      width: 200,
      contentPadding: const EdgeInsets.all(4),
      selectedBorder: Border.all(color: Colors.white),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Column(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              InPortWidget(
                name: 'PortIn1',
                onConnect: (String name, String port) => true,
                icon: const Icon(
                  Icons.circle_outlined,
                  color: Colors.yellowAccent,
                  size: 20,
                ),
                iconConnected: const Icon(
                  Icons.circle,
                  color: Colors.yellowAccent,
                  size: 20,
                ),
                multiConnections: false,
                connectionTheme:
                    ConnectionTheme(color: Colors.yellowAccent, strokeWidth: 2),
              ),
            ],
          ),
          const Icon(Icons.safety_divider),
          OutPortWidget(
            name: 'PortOut1',
            icon: Transform.flip(
              flipX: true,
              child: const Icon(
                Icons.arrow_back,
                color: Colors.blue,
                size: 24,
              ),
            ),
            iconConnected: const Icon(
              Icons.pause_circle,
              color: Colors.deepOrange,
              size: 24,
            ),
            multiConnections: false,
            connectionTheme:
                ConnectionTheme(color: Colors.deepOrange, strokeWidth: 2),
          ),
        ],
      ),
    );
  }
}
