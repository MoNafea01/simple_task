import 'package:ai_gen/helper/helper.dart';
import 'package:ai_gen/sonnet_code.dart';
import 'package:flutter/material.dart';
import 'package:vs_node_view/data/standard_interfaces/vs_int_interface.dart';
import 'package:vs_node_view/vs_node_view.dart';

class VSHelper {
  static List<Object> nodeBuilders = [
    VSSubgroup(
      name: "Numbers",
      subgroup: [
        (Offset offset, VSOutputData? ref) => VSNodeData(
              type: "Parse int",
              widgetOffset: offset,
              inputData: [
                VSStringInputData(
                  type: "Input",
                  initialConnection: ref,
                )
              ],
              outputData: [
                VSIntOutputData(
                  type: "Output",
                  outputFunction: (data) => int.parse(data["Input"]),
                ),
              ],
            ),
        (Offset offset, VSOutputData? ref) => VSNodeData(
              type: "Sum",
              widgetOffset: offset,
              inputData: [
                VSNumInputData(
                  type: "Input 1",
                  initialConnection: ref,
                ),
                VSNumInputData(
                  type: "Input 2",
                  initialConnection: ref,
                )
              ],
              outputData: [
                VSNumOutputData(
                  type: "output",
                  outputFunction: (data) {
                    return (data["Input 1"] ?? 0) + (data["Input 2"] ?? 0);
                  },
                ),
              ],
            ),
      ],
    ),
    VSSubgroup(
      name: "Logic",
      subgroup: [
        (Offset offset, VSOutputData? ref) => VSNodeData(
              type: "Bigger than",
              widgetOffset: offset,
              inputData: [
                VSNumInputData(
                  type: "First",
                  initialConnection: ref,
                ),
                VSNumInputData(
                  type: "Second",
                  initialConnection: ref,
                ),
              ],
              outputData: [
                VSBoolOutputData(
                  type: "Output",
                  outputFunction: (data) => data["First"] > data["Second"],
                ),
              ],
            ),
        (Offset offset, VSOutputData? ref) => VSNodeData(
              type: "If",
              widgetOffset: offset,
              inputData: [
                VSBoolInputData(
                  type: "Input",
                  initialConnection: ref,
                ),
                VSDynamicInputData(
                  type: "True",
                  initialConnection: ref,
                ),
                VSDynamicInputData(
                  type: "False",
                  initialConnection: ref,
                ),
              ],
              outputData: [
                VSDynamicOutputData(
                  type: "Output",
                  outputFunction: (data) =>
                      data["Input"] ? data["True"] : data["False"],
                ),
              ],
            ),
      ],
    ),
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
        type: "Input",
        widgetOffset: offset,
        outputData: VSStringOutputData(
          type: "Output",
          outputFunction: (data) => controller.text,
        ),
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
        type: "ListInput",
        widgetOffset: offset,
        outputData: VSListOutputData(
          type: "Output",
          outputFunction: (data) async => Helper.parseList(controller.text),
        ),
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
    (Offset offset, VSOutputData<dynamic>? ref) {
      print(ref?.nodeData?.inputData.toList());

      return VSNodeData(
        type: "train Test Split",
        widgetOffset: offset,
        inputData: [
          VSListInputData(
            type: "data",
            initialConnection: ref,
          ),
          VSDoubleInputData(
            type: "test_size",
            initialConnection: ref,
          ),
          VSDoubleInputData(
            type: "random_state",
            initialConnection: ref,
          ),
        ],
        outputData: [
          VSListOutputData(
            type: "X_train",
            outputFunction: (data) {
              // Explicitly type the List as List<double>
              return trainTestSplit(data["data"])
                  .then<List<double>>((result) => result['X_train'] ?? [])
                  .catchError((error) => []); // Explicitly return List<double>
            },
          ),
          VSListOutputData(
            type: "X_test",
            outputFunction: (data) {
              return trainTestSplit(data["data"])
                  .then<List<double>>((result) => result['X_test'] ?? [])
                  .catchError((error) => []); // Explicitly return List<double>
            },
          ),
        ],
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
        outputData: VSDoubleOutputData(
          type: "Output",
          outputFunction: (data) => double.parse(controller.text),
        ),
        child: Expanded(child: input),
        setValue: (value) => controller.text = value,
        getValue: () => controller.text,
      );
    },
  ];
}
