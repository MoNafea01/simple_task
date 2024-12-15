import 'package:ai_gen/block_view/node_builder/models_subgroup.dart';
import 'package:ai_gen/functions/create_model.dart';
import 'package:ai_gen/functions/train_test_split.dart';
import 'package:ai_gen/helper/helper.dart';
import 'package:ai_gen/vs_node_view/custom_widgets/vs_text_input_data.dart';
import 'package:ai_gen/vs_node_view/data/standard_interfaces/vs_list_interface.dart';
import 'package:ai_gen/vs_node_view/data/standard_interfaces/vs_model_interface.dart';
import 'package:ai_gen/vs_node_view/vs_node_view.dart';
import 'package:flutter/material.dart';

class NodeBuilder {
  static List<Object> nodeBuilders = [
    // numbersSubGroup(),
    ModelsSubGroup(),

    (Offset offset, VSOutputData<dynamic>? ref) {
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
    },
    (Offset offset, VSOutputData<dynamic>? ref) {
      final modelNameController = TextEditingController()..text = "0.5";
      final modelTypeController = TextEditingController()..text = "2";
      final taskController = TextEditingController()..text = "2";
      final paramsController = TextEditingController()..text = "2";
      return VSWidgetNode(
        type: "Create Model",
        widgetOffset: offset,
        setValue: (value) {},
        getValue: () => "",
        inputData: [
          VsTextInputData(
            type: "Model Name",
            controller: modelNameController,
          ),
          VsTextInputData(
            type: "Model Type",
            controller: modelTypeController,
          ),
          VsTextInputData(
            controller: taskController,
            type: "Task",
          ),
          VsTextInputData(
            controller: paramsController,
            type: "Params",
          ),
        ],
        outputData: [
          VSModelOutputData(
            type: "Model",
            outputFunction: (data) async {
              final splitDataFuture = await createModel({
                "model_name": modelNameController.text,
                "model_type": modelTypeController.text,
                "task": taskController.text,
                "params": paramsController.text,
              });

              return splitDataFuture;
            },
          ),
        ],
      );
    },

    (Offset offset, VSOutputData? ref) {
      final TextEditingController controller = TextEditingController();
      final TextField input = TextField(
        controller: controller,
        decoration: const InputDecoration(
          isDense: true,
          contentPadding: EdgeInsets.symmetric(horizontal: 0, vertical: 10),
        ),
      );

      return VSWidgetNode(
        type: "ListInput",
        widgetOffset: offset,
        outputData: [
          VSListOutputData(
            type: "Output",
            outputFunction: (data) => Helper.parseList(controller.text),
          ),
        ],
        child: Expanded(child: input),
        setValue: (value) => controller.text = value,
        getValue: () => controller.text,
      );
    },

    (Offset offset, VSOutputData? ref) {
      final controller = TextEditingController();
      final input = TextField(
        controller: controller,
        decoration: const InputDecoration(
          isDense: true,
          contentPadding: EdgeInsets.symmetric(horizontal: 0, vertical: 10),
        ),
      );

      return VSWidgetNode(
        type: "Double input",
        widgetOffset: offset,
        outputData: [
          VSDoubleOutputData(
            type: "Output",
            outputFunction: (data) => double.parse(controller.text),
          ),
        ],
        child: Expanded(child: input),
        setValue: (value) => controller.text = value,
        getValue: () => controller.text,
      );
    },
    (Offset offset, VSOutputData? ref) {
      final controller = TextEditingController();
      final input = TextField(
        controller: controller,
        decoration: const InputDecoration(
          isDense: true,
          contentPadding: EdgeInsets.symmetric(horizontal: 0, vertical: 10),
        ),
      );

      return VSWidgetNode(
        type: "int input",
        widgetOffset: offset,
        outputData: [
          VSIntOutputData(
            type: "Output",
            outputFunction: (data) => int.parse(controller.text),
          ),
        ],
        child: Expanded(child: input),
        setValue: (value) => controller.text = value,
        getValue: () => controller.text,
      );
    },
    (Offset offset, VSOutputData? ref) => VSOutputNode(
          type: "Output",
          widgetOffset: offset,
          ref: ref,
        ),
    // (Offset offset, VSOutputData<dynamic>? ref) {
    //   Future<Map<String, List<double>>>? splitDataFuture;
    //   TextEditingController controller = TextEditingController();
    //   return VSNodeData(
    //     type: "textField train Test Split",
    //     widgetOffset: offset,
    //     inputData: [
    //       VSListInputData(
    //         type: "data",
    //         initialConnection: ref,
    //       ),
    //       VSDoubleInputData(
    //         type: "test_size",
    //         initialConnection: ref,
    //       ),
    //       VSIntInputData(
    //         interfaceIconBuilder: (context, anchor, data) {
    //           return SizedBox(
    //             width: 20,
    //             height: 20,
    //             child: TextField(controller: controller),
    //           );
    //         },
    //         title: "random",
    //         toolTip: "hello",
    //         type: "random_state",
    //         initialConnection: VSIntOutputData(
    //           type: "int",
    //           outputFunction: (p0) => int.parse(controller.text),
    //         ),
    //       ),
    //     ],
    //     outputData: [
    //       VSListOutputData(
    //         type: "X_train",
    //         outputFunction: (data) async {
    //           print(data);
    //           data["data"] = await data["data"];
    //
    //           splitDataFuture = trainTestSplit(
    //             data["data"],
    //             testSize: data["test_size"] ?? 0.5,
    //             randomState: data["random_state"] ?? 2,
    //           );
    //           Map<String, List<double>> splitData = await splitDataFuture!;
    //
    //           return splitData['X_train']!;
    //         },
    //       ),
    //       VSListOutputData(
    //         type: "X_test",
    //         outputFunction: (data) async {
    //           data["data"] = await data["data"];
    //
    //           splitDataFuture ??= trainTestSplit(data["data"]);
    //
    //           Map<String, List<double>> splitData = await splitDataFuture!;
    //
    //           return splitData['X_test']!;
    //         },
    //       ),
    //     ],
    //   );
    // },
  ];
}
// VSSubgroup(
//   name: "Logic",
//   subgroup: [
//     (Offset offset, VSOutputData? ref) => VSNodeData(
//           type: "Bigger than",
//           widgetOffset: offset,
//           inputData: [
//             VSNumInputData(
//               type: "First",
//               initialConnection: ref,
//             ),
//             VSNumInputData(
//               type: "Second",
//               initialConnection: ref,
//             ),
//           ],
//           outputData: [
//             VSBoolOutputData(
//               type: "Output",
//               outputFunction: (data) => data["First"] > data["Second"],
//             ),
//           ],
//         ),
//     (Offset offset, VSOutputData? ref) => VSNodeData(
//           type: "If",
//           widgetOffset: offset,
//           inputData: [
//             VSBoolInputData(
//               type: "Input",
//               initialConnection: ref,
//             ),
//             VSDynamicInputData(
//               type: "True",
//               initialConnection: ref,
//             ),
//             VSDynamicInputData(
//               type: "False",
//               initialConnection: ref,
//             ),
//           ],
//           outputData: [
//             VSDynamicOutputData(
//               type: "Output",
//               outputFunction: (data) =>
//                   data["Input"] ? data["True"] : data["False"],
//             ),
//           ],
//         ),
//   ],
// ),
// (Offset offset, VSOutputData? ref) {
//   final controller = TextEditingController();
//   final input = TextField(
//     controller: controller,
//     decoration: const InputDecoration(
//       isDense: true,
//       contentPadding: EdgeInsets.symmetric(horizontal: 0, vertical: 10),
//     ),
//   );
//
//   return VSWidgetNode(
//     type: "Input",
//     widgetOffset: offset,
//     outputData: VSStringOutputData(
//       type: "Output",
//       outputFunction: (data) => controller.text,
//     ),
//     child: Expanded(child: input),
//     setValue: (value) => controller.text = value,
//     getValue: () => controller.text,
//   );
// },
// (Offset offset, VSOutputData<dynamic>? ref) {
//   Future<Map<String, List<double>>>? splitDataFuture;
//   return VSNodeData(
//     type: "train Test Split",
//     widgetOffset: offset,
//     inputData: [
//       VSListInputData(
//         type: "data",
//         initialConnection: ref,
//       ),
//       VSDoubleInputData(
//         type: "test_size",
//         initialConnection: ref,
//       ),
//       VSIntInputData(
//         type: "random_state",
//         initialConnection: ref,
//       ),
//     ],
//     outputData: [
//       VSListOutputData(
//         type: "X_train",
//         outputFunction: (data) async {
//           data["data"] = await data["data"];
//
//           splitDataFuture = trainTestSplit(
//             data["data"],
//             testSize: data["test_size"] ?? 0.5,
//             randomState: data["random_state"] ?? 2,
//           );
//           Map<String, List<double>> splitData = await splitDataFuture!;
//
//           return splitData['X_train']!;
//         },
//       ),
//       VSListOutputData(
//         type: "X_test",
//         outputFunction: (data) async {
//           data["data"] = await data["data"];
//
//           splitDataFuture ??= trainTestSplit(data["data"]);
//
//           Map<String, List<double>> splitData = await splitDataFuture!;
//
//           return splitData['X_test']!;
//         },
//       ),
//     ],
//   );
// },
