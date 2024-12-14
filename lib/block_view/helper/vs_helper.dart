import 'package:ai_gen/helper/helper.dart';
import 'package:ai_gen/sonnet_code.dart';
import 'package:ai_gen/vs_node_view/data/standard_interfaces/vs_list_interface.dart';
import 'package:ai_gen/vs_node_view/vs_node_view.dart';
import 'package:flutter/material.dart';


//click right
// VSSubgroup -----> 

/*
The VSHelper class serves as a collection of building blocks for a visual programming environment,
 allowing users to create data processing flows by connecting different nodes that perform specific operations.
  Each node is designed to handle specific types of data and operations, making it easier to build complex logic visually.


*/


class VSHelper {

  static List<Object> nodeBuilders = [

// VSSubgroup contains a group of blocks inside it

    VSSubgroup(
      name: "Numbers",
      subgroup: [

// first block in Numbers ----> VSNodeData

        (Offset offset, VSOutputData? ref) => VSNodeData(
              type: "Parse int",
              widgetOffset: offset,
              inputData: [
                VSStringInputData(    //class extend from VSInputData
                                      // take string value
                  type: "Input",
                  initialConnection: ref,  //default connetion ti this intrface 
                ),
              ],
              outputData: [
                VSIntOutputData(      //class extend from VSOutputData
                  type: "Output",
                  outputFunction: (data) => int.parse(data["Input"]),   //{FutureOr<int> Function(Map<String, dynamic>)? outputFunction}
                                                                        // transform the string value to integer value.
                ),
              ],
            ),


// second block in Numbers ----> VSNodeData


//Sum: Takes two numbers and returns their sum.
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


    // first group in the list



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



//Train Test Split Node:
//Accepts a dataset, a test size, and a random state, and outputs the training and testing datasets



    (Offset offset, VSOutputData<dynamic>? ref) {
      Future<Map<String, List<double>>>? splitDataFuture;
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
          VSIntInputData(
            type: "random_state",
            initialConnection: ref,
          ),
        ],
        outputData: [
          VSListOutputData(
            type: "X_train",
            outputFunction: (data) async {
              data["data"] = await data["data"];

              splitDataFuture = trainTestSplit(     // trainTestSplit ---> api call
               
                data["data"],
                testSize: data["test_size"] ?? 0.5,
                randomState: data["random_state"] ?? 2,
              );

//  splitDataFuture ----> /*
/*
 {
      'X_train': List<double>.from(jsonResponse['X_train']),
      'X_test': List<double>.from(jsonResponse['X_test']),
    }

              */

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

///////////////////////////////////////////////////////////////////////////////////////////////////


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
          outputFunction: (data) => Helper.parseList(controller.text),
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
        outputData: VSIntOutputData(
          type: "Output",
          outputFunction: (data) => int.parse(controller.text),
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
