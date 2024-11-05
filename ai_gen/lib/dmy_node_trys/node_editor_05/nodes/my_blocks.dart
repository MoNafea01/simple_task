import 'package:flutter/material.dart';

import '../class/node_data.dart';
import '../my_node_editor/node_editor.dart';

NodeWidgetBase printerNode(
  String name,
  FocusNode focusNode,
  TextEditingController controller,
) {
  return TitleBarNodeWidget(
    name: name,
    typeName: 'printer',
    backgroundColor: Colors.black87,
    radius: 10,
    selectedBorder: Border.all(color: Colors.white),
    title: const Text('Print'),
    iconTileSpacing: 5,
    titleBarPadding: const EdgeInsets.all(4.0),
    titleBarGradient: const LinearGradient(
        colors: [Color.fromRGBO(12, 100, 6, 1.0), Colors.greenAccent]),
    icon: const Icon(Icons.receipt_rounded, color: Colors.white),
    width: 200,
    child: Column(
      crossAxisAlignment: CrossAxisAlignment.end,
      children: [
        Row(
          mainAxisAlignment: MainAxisAlignment.start,
          children: [
            InPortWidget(
              name: 'PortIn',
              onConnect: (String _name, String port) {
                print("block  ${name}  is connected to $_name -- port $port ");
                return true;
              },
              icon: const Icon(
                Icons.play_arrow_outlined,
                color: Colors.red,
                size: 24,
              ),
              iconConnected: const Icon(
                Icons.play_arrow,
                color: Colors.red,
                size: 24,
              ),
              multiConnections: false,
              connectionTheme:
                  ConnectionTheme(color: Colors.red, strokeWidth: 2),
              onDataReceived: (data) {
                // Update node data based on received input
                print('Data received: ${data.value}');
              },
            ),
            const Text('Input 1'),
          ],
        ),
      ],
    ),
  );
}

NodeWidgetBase myComponentNode(
  String name,
  FocusNode focusNode,
  TextEditingController controller,
) {
  return TitleBarNodeWidget(
    name: name,
    typeName: 'node_1',
    backgroundColor: Colors.black87,
    radius: 10,
    selectedBorder: Border.all(color: Colors.white),
    title: const Text('Text'),
    iconTileSpacing: 5,
    titleBarPadding: const EdgeInsets.all(4.0),
    titleBarGradient: const LinearGradient(
        colors: [Color.fromRGBO(0, 23, 135, 1.0), Colors.lightBlue]),
    icon: const Icon(
      Icons.rectangle_outlined,
      color: Colors.white,
    ),
    width: 200,
    child: Column(
      crossAxisAlignment: CrossAxisAlignment.end,
      children: [
        Padding(
          padding: const EdgeInsets.all(8.0),
          child: TextEditProperty(
            name: 'text_prop',
            focusNode: focusNode,
            controller: controller,
            style: const TextStyle(
                color: Colors.white,
                fontWeight: FontWeight.normal,
                fontSize: 14),
            decoration: InputDecoration(
              filled: true,
              contentPadding:
                  const EdgeInsets.symmetric(vertical: 0.0, horizontal: 5.0),
              fillColor: Colors.white10,
              border: OutlineInputBorder(
                  borderSide: const BorderSide(color: Colors.white),
                  borderRadius: BorderRadius.circular(5)),
            ),
          ),
        ),
        Row(
          mainAxisAlignment: MainAxisAlignment.end,
          children: [
            const Text('Output 3'),
            OutPortWidget(
              name: 'PortOut3',
              icon: const Icon(
                Icons.play_arrow_outlined,
                color: Colors.green,
                size: 24,
              ),
              iconConnected: const Icon(
                Icons.play_arrow,
                color: Colors.green,
                size: 24,
              ),
              multiConnections: false,
              connectionTheme:
                  ConnectionTheme(color: Colors.green, strokeWidth: 2),
              onDataRequest: () {
                // Provide data to be sent to connected nodes
                return NodeData('Output data');
              },
            ),
          ],
        ),
      ],
    ),
  );
}
