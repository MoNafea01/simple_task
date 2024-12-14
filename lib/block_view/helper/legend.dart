import 'package:ai_gen/vs_node_view/vs_node_view.dart';
import 'package:flutter/material.dart';
// الالوان ال تحت علي اليمين

class Legend extends StatelessWidget {
  const Legend({super.key});

  @override
  Widget build(BuildContext context) {
    final List<Widget> widgets = [];

    Map<String, Color> inputTypes = {
      "String": VSStringInputData(type: "legend").interfaceColor,
      "Int": VSIntInputData(type: "legend").interfaceColor,
      "Double": VSDoubleInputData(type: "legend").interfaceColor,
      "Num": VSNumInputData(type: "legend").interfaceColor,
      "Bool": VSBoolInputData(type: "legend").interfaceColor,
      "Dynamic": VSDynamicInputData(type: "legend").interfaceColor,
    };

    final Iterable<MapEntry<String, Color>> entries = inputTypes.entries;

    for (final entry in entries) {
      widgets.add(
        Row(
          children: [
            Text(entry.key),
            const SizedBox(width: 5,),
            Icon(
              Icons.circle,
              color: entry.value,
            ),
            if (entry != entries.last) const Divider(),
          ],
        ),
      );
    }

    return Card(
        child: Padding(
      padding: const EdgeInsets.all(8.0),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.end,
        children: widgets,
      ),
    ),
    );
  }
}
