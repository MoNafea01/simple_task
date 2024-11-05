import 'package:flutter/material.dart';

import 'my_node_red/node_editor.dart';

class MyNodeGrid extends StatelessWidget {
  const MyNodeGrid({
    super.key,
    required FocusNode focusNode,
    required NodeEditorController controller,
  })  : _focusNode = focusNode,
        _controller = controller;

  final FocusNode _focusNode;
  final NodeEditorController _controller;

  @override
  Widget build(BuildContext context) {
    return InteractiveViewer(
      constrained: false,
      child: SizedBox(
        height: 5000,
        width: 5000,
        child: NodeEditor(
          infiniteCanvasSize: 5000,
          focusNode: _focusNode,
          controller: _controller,
          background: const GridBackground(),
        ),
      ),
    );
  }
}
