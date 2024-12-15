import 'package:ai_gen/features/node_view/data/functions/train_test_split.dart';
import 'package:ai_gen/node_package/custom_widgets/vs_text_input_data.dart';
import 'package:ai_gen/node_package/data/standard_interfaces/vs_list_interface.dart';
import 'package:ai_gen/node_package/data/vs_interface.dart';
import 'package:ai_gen/node_package/data/vs_subgroup.dart';
import 'package:ai_gen/node_package/special_nodes/vs_widget_node.dart';
import 'package:flutter/material.dart';

class FunctionsSubgroup extends VSSubgroup {
  FunctionsSubgroup()
      : super(
          name: "Functions",
          subgroup: [
            _trainTestSplit,
          ],
        );

  static VSWidgetNode _trainTestSplit(
      Offset offset, VSOutputData<dynamic>? ref) {
    Future<Map<String, List<double>>>? splitDataFuture;
    final testSizeController = TextEditingController()..text = "0.5";
    final randomStateController = TextEditingController()..text = "2";
    return VSWidgetNode(
      type: "train Test Split",
      widgetOffset: offset,
      setValue: (value) {},
      getValue: () => "",
      inputData: [
        VSListInputData(
          type: "data",
          initialConnection: ref,
        ),
        VsTextInputData(
          type: "test_size",
          controller: testSizeController,
        ),
        VsTextInputData(
          controller: randomStateController,
          type: "random_state",
        ),
      ],
      outputData: [
        VSListOutputData(
          type: "X_train",
          outputFunction: (data) async {
            data["data"] = await data["data"];
            splitDataFuture = trainTestSplit(
              data["data"],
              testSize: double.parse(testSizeController.text),
              randomState: int.parse(randomStateController.text),
            );
            Map<String, List<double>> splitData = await splitDataFuture!;

            return splitData['X_train']!;
          },
        ),
        VSListOutputData(
          type: "X_test",
          outputFunction: (data) async {
            data["data"] = await data["data"];

            splitDataFuture ??= trainTestSplit(data["data"]);

            Map<String, List<double>> splitData = await splitDataFuture!;

            return splitData['X_test']!;
          },
        ),
      ],
    );
  }
}
