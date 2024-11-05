import 'package:flutter/material.dart';

import 'my_node_editor/node_editor.dart';
import 'nodes/my_blocks.dart';

class MyNodeEditor extends StatefulWidget {
  const MyNodeEditor({super.key});

  @override
  State<MyNodeEditor> createState() => _MyNodeEditorState();
}

class _MyNodeEditorState extends State<MyNodeEditor>
    with PropertyMixin<String> {
  final NodeEditorController controller = NodeEditorController();
  final FocusNode _focusNode = FocusNode();
  final FocusNode comp_focusNode = FocusNode();
  final FocusNode _focusNode2 = FocusNode();
  final TextEditingController _controller = TextEditingController();
  final TextEditingController comp_controller = TextEditingController();
  @override
  void initState() {
    controller.addSelectListener((Connection conn) {
      debugPrint("ON SELECT inNode: ${conn.inNode}, inPort: ${conn.inPort}");
    });

    controller.addNode(
      myComponentNode(
        'node_1_1',
        comp_focusNode,
        comp_controller,
      ),
      NodePosition.afterLast,
    );
    controller.addNode(
      printerNode('print_1', _focusNode2, _controller),
      NodePosition.afterLast,
    );
    // controller.addNode(
    //   componentNode('node_1_3'),
    //   NodePosition.afterLast,
    // );
    // controller.addNode(
    //   receiverNode('node_2_1', _focusNode2, _controller),
    //   NodePosition.afterLast,
    // );
    // controller.addNode(
    //   binaryNode('node_3_1'),
    //   NodePosition.afterLast,
    // );
    // controller.addNode(
    //   sinkNode('node_4_1'),
    //   NodePosition.afterLast,
    // );
    super.initState();
  }

  void _addNewNode() {
    controller.addNode(
      printerNode('print_1', _focusNode2, _controller),
      NodePosition.afterLast,
    );
  }

  @override
  void dispose() {
    _focusNode.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text("Demo Nodes"),
        actions: [
          IconButton(
              onPressed: () {
                debugPrint('controller.toMap(): ${controller.toJson()}');
              },
              icon: const Icon(Icons.abc))
        ],
      ),
      body: NodeEditor(
        focusNode: _focusNode,
        controller: controller,
        background: const GridBackground(),
        infiniteCanvasSize: 5000,
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _addNewNode,
        child: const Icon(Icons.add),
      ),
    );
  }
}
