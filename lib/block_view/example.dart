import 'dart:developer';

import 'package:ai_gen/vs_node_view/vs_node_view.dart';
import 'package:flutter/material.dart';

import 'helper/legend.dart';
import 'helper/vs_helper.dart';


//  الواجهه التي تظهر في البدايه 

/*
 The VSNodeExample widget provides a visual interface for users to work with nodes that perform various operations.
  It allows for dynamic interaction and evaluation of node outputs,
   making it a useful tool for visual programming and data processing tasks. 
 */

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
        // لما بدوس كليك يمين القائمه ال بتفتح 
        
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
          top: 50,
          right: 10,
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.end,
            children: [
              ElevatedButton(
                onPressed: () async {
                  List<MapEntry<String, dynamic>> entries =
                      nodeDataProvider.nodeManager.getOutputNodes
                          .map(
                            (e) => e.evaluate(
                                // onError: (_, __) => Future.delayed(Duration.zero, () {
                                //   print("Error : ${_.toString()}");
                                // }),
                                ),
                          )
                          .toList();
                  log("entries: $entries");
                  for (var i = 0; i < entries.length; i++) {
                    var asyncOutput = await entries[i].value;
                    entries[i] = MapEntry(entries[i].key, asyncOutput);
                  }

                  results = entries.map((e) {
                    return "${e.key}: ${e.value}";
                  });
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

// import 'dart:developer';

// import 'package:ai_gen/vs_node_view/vs_node_view.dart';
// import 'package:flutter/material.dart';

// import 'helper/legend.dart';
// import 'helper/vs_helper.dart';

// // The main UI for your app

// class VSNodeExample extends StatefulWidget {
//   const VSNodeExample({super.key});

//   @override
//   State<VSNodeExample> createState() => _VSNodeExampleState();
// }

// class _VSNodeExampleState extends State<VSNodeExample> {
//   Iterable<String>? results;

//   VSNodeDataProvider nodeDataProvider = VSNodeDataProvider(
//     nodeManager: VSNodeManager(nodeBuilders: VSHelper.nodeBuilders),
//   );

//   @override
//   void initState() {
//     super.initState();
//     _evaluateNodes(); // Evaluate nodes on app startup
//   }

//   // Function to evaluate nodes and update results
//   Future<void> _evaluateNodes() async {
//     List<MapEntry<String, dynamic>> entries =
//         nodeDataProvider.nodeManager.getOutputNodes
//             .map(
//               (e) => e.evaluate(
//                   // Add error handling if needed
//                   ),
//             )
//             .toList();

//     log("entries: $entries");
//     for (var i = 0; i < entries.length; i++) {
//       var asyncOutput = await entries[i].value;
//       entries[i] = MapEntry(entries[i].key, asyncOutput);
//     }

//     results = entries.map((e) {
//       return "${e.key}: ${e.value}";
//     });
//     setState(() {}); // Update the UI with the evaluated results
//   }

//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       body: Row(
//         children: [
//           // Left Panel: List of blocks
//           Container(
//             width: 300,
//             color: Colors.grey[200],
//             child: Column(
//               crossAxisAlignment: CrossAxisAlignment.stretch,
//               children: [
//                 const Padding(
//                   padding: EdgeInsets.all(8.0),
//                   child: Text(
//                     "Blocks",
//                     style: TextStyle(
//                       fontSize: 20,
//                       fontWeight: FontWeight.bold,
//                     ),
//                   ),
//                 ),
//                 if (results != null)
//                   ...results!.map(
//                     (e) => Card(
//                       child: Padding(
//                         padding: const EdgeInsets.all(8.0),
//                         child: Text(e),
//                       ),
//                     ),
//                   )
//                 else
//                   const Center(child: CircularProgressIndicator()), // Loading indicator while results load
//               ],
//             ),
//           ),

//           // Right Panel: Main interactive view
//           Expanded(
//             child: Stack(
//               children: [
//                 InteractiveVSNodeView(
//                   width: 5000,
//                   height: 5000,
//                   nodeDataProvider: nodeDataProvider,
//                 ),
//                 const Positioned(
//                   bottom: 0,
//                   right: 0,
//                   child: Legend(),
//                 ),
//                 Positioned(
//                   top: 10,
//                   right: 0,
//                   child: ElevatedButton(
//                     onPressed: _evaluateNodes,
//                     child: const Text("Evaluate"),
//                   ),
//                 ),
//               ],
//             ),
//           ),
//         ],
//       ),
//     );
//   }
// }


// import 'dart:developer';

// import 'package:ai_gen/vs_node_view/vs_node_view.dart';
// import 'package:flutter/material.dart';

// import 'helper/legend.dart';
// import 'helper/vs_helper.dart';

// class VSNodeExample extends StatefulWidget {
//   const VSNodeExample({super.key});

//   @override
//   State<VSNodeExample> createState() => _VSNodeExampleState();
// }

// class _VSNodeExampleState extends State<VSNodeExample> {
//   Iterable<String>? results;

//   VSNodeDataProvider nodeDataProvider = VSNodeDataProvider(
//     nodeManager: VSNodeManager(nodeBuilders: VSHelper.nodeBuilders),
//   );

//   @override
//   void initState() {
//     super.initState();
//     _evaluateNodes(); // Evaluate nodes at startup
//   }

//   // Function to evaluate and populate the block list
//   Future<void> _evaluateNodes() async {
//     List<MapEntry<String, dynamic>> entries =
//         nodeDataProvider.nodeManager.getOutputNodes.map(
//       (node) {
//         return node.evaluate(
//             // Add error handling here if needed
//             );
//       },
//     ).toList();

//     log("Entries found: $entries");
//     for (int i = 0; i < entries.length; i++) {
//       var asyncOutput = await entries[i].value;
//       entries[i] = MapEntry(entries[i].key, asyncOutput);
//     }

//     results = entries.map((e) => "${e.key}: ${e.value}");
//     setState(() {});
//   }

//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       body: Row(
//         children: [
//           // Left Side: Block list
//           Container(
//             width: 300,
//             color: Colors.grey[200],
//             child: Column(
//               crossAxisAlignment: CrossAxisAlignment.stretch,
//               children: [
//                 const Padding(
//                   padding: EdgeInsets.all(8.0),
//                   child: Text(
//                     "Blocks",
//                     style: TextStyle(
//                       fontSize: 20,
//                       fontWeight: FontWeight.bold,
//                     ),
//                   ),
//                 ),
//                 // Display blocks or loading state
//                 Expanded(
//                   child: results != null
//                       ? ListView(
//                           children: results!
//                               .map(
//                                 (block) => Card(
//                                   child: ListTile(
//                                     title: Text(block),
//                                   ),
//                                 ),
//                               )
//                               .toList(),
//                         )
//                       : const Center(child: CircularProgressIndicator()),
//                 ),
//               ],
//             ),
//           ),

//           // Right Side: Interactive View
//           Expanded(
//             child: Stack(
//               children: [
//                 InteractiveVSNodeView(
//                   width: 5000,
//                   height: 5000,
//                   nodeDataProvider: nodeDataProvider,
//                 ),
//                 const Positioned(
//                   bottom: 0,
//                   right: 0,
//                   child: Legend(),
//                 ),
//                 Positioned(
//                   top: 10,
//                   right: 0,
//                   child: ElevatedButton(
//                     onPressed: _evaluateNodes, // Re-evaluate nodes
//                     child: const Text("Evaluate"),
//                   ),
//                 ),
//               ],
//             ),
//           ),
//         ],
//       ),
//     );
//   }
// }


// import 'package:ai_gen/vs_node_view/data/vs_node_data_provider.dart';
// import 'package:ai_gen/vs_node_view/data/vs_node_manager.dart';
// import 'package:ai_gen/vs_node_view/data/vs_subgroup.dart';
// import 'package:ai_gen/vs_node_view/widgets/interactive_vs_node_view.dart';
// import 'package:flutter/material.dart';
// import 'package:ai_gen/vs_node_view/vs_node_view.dart';// Import your VSNodeView files  vs_node_view
// import 'helper/vs_helper.dart';

// class VSNodeExample extends StatefulWidget {
//   const VSNodeExample({super.key});

//   @override
//   State<VSNodeExample> createState() => _VSNodeExampleState();
// }

// class _VSNodeExampleState extends State<VSNodeExample> {
//   VSNodeDataProvider nodeDataProvider = VSNodeDataProvider(
//     nodeManager: VSNodeManager(nodeBuilders: VSHelper.nodeBuilders),
//   );

//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       body: Row(
//         children: [
//           // Left Panel: Display the list of groups and their blocks
//           Container(
//             width: 300,
//             color: Colors.grey[200],
//             child: ListView(
//               children: [
//                 for (var builder in VSHelper.nodeBuilders)
//                   if (builder is VSSubgroup)
//                     ExpansionTile(
//                       title: Text(builder.name),
//                       children: [
//                         for (var block in builder.subgroup)
//                           ListTile(
//                             title: Text(block.runtimeType.toString()),
//                             onTap: () {
//                               // Add a new block to the interactive view
//                               setState(() {
//                                 nodeDataProvider.nodeManager.addNode(
//                                   block(const Offset(100, 100), null),
//                                 );
//                               });
//                             },
//                           ),
//                       ],
//                     )
//               ],
//             ),
//           ),

//           // Right Panel: Interactive Node View
//           Expanded(
//             child: Stack(
//               children: [
//                 InteractiveVSNodeView(
//                   width: 5000,
//                   height: 5000,
//                   nodeDataProvider: nodeDataProvider,
//                 ),
//               ],
//             ),
//           ),
//         ],
//       ),
//     );
//   }
// }
// import 'package:ai_gen/vs_node_view/data/vs_node_data.dart';
// import 'package:ai_gen/vs_node_view/data/vs_node_data_provider.dart';
// import 'package:ai_gen/vs_node_view/data/vs_node_manager.dart';
// import 'package:ai_gen/vs_node_view/data/vs_subgroup.dart';
// import 'package:ai_gen/vs_node_view/widgets/interactive_vs_node_view.dart';
// import 'package:flutter/material.dart';
// //import 'vs_node_view.dart'; // Import your VSNodeView files
// import 'helper/vs_helper.dart';

// class VSNodeExample extends StatefulWidget {
//   const VSNodeExample({super.key});

//   @override
//   State<VSNodeExample> createState() => _VSNodeExampleState();
// }

// class _VSNodeExampleState extends State<VSNodeExample> {
//   VSNodeDataProvider nodeDataProvider = VSNodeDataProvider(
//     nodeManager: VSNodeManager(nodeBuilders: VSHelper.nodeBuilders),
//   );

//   // Function to add a node dynamically
//   void _addNode() {
//     VSNodeData newNode = VSNodeData(
//       type: "Dynamic Node",
//       widgetOffset: const Offset(100, 100), // Position of the node
//       inputData: [],
//       outputData: [],
//     );

//     nodeDataProvider.nodeManager.updateOrCreateNodes([newNode]);
//     setState(() {}); // Refresh the UI to reflect the changes
//   }

//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       body: Row(
//         children: [
//           // Left Panel: Display the list of groups and their blocks
//           Container(
//             width: 300,
//             color: Colors.grey[200],
//             child: ListView(
//               children: [
//                 for (var builder in VSHelper.nodeBuilders)
//                   if (builder is VSSubgroup)
//                     ExpansionTile(
//                       title: Text(builder.name),
//                       children: [
//                         for (var block in builder.subgroup)
//                           ListTile(
//                             title: Text(block.runtimeType.toString()),
//                             onTap: () {
//                               // Add a new block to the interactive view
//                               setState(() {
//                                 _addNode(); // Add node dynamically
//                               });
//                             },
//                           ),
//                       ],
//                     )
//               ],
//             ),
//           ),

//           // Right Panel: Interactive Node View
//           Expanded(
//             child: Stack(
//               children: [
//                 InteractiveVSNodeView(
//                   width: 5000,
//                   height: 5000,
//                   nodeDataProvider: nodeDataProvider,
//                 ),
//               ],
//             ),
//           ),
//         ],
//       ),
//     );
//   }
// }


// import 'package:ai_gen/block_view/helper/vs_helper.dart';
// import 'package:ai_gen/vs_node_view/data/vs_subgroup.dart';
// import 'package:ai_gen/vs_node_view/widgets/interactive_vs_node_view.dart';
// import 'package:flutter/material.dart';

// @override
// Widget build(BuildContext context) {
//   return Scaffold(
//     appBar: AppBar(
//       title: Text('ai_gen'),
//     ),
//     body: Row(
//       children: [
//         // Left Panel: Display list of node categories and nodes
//         Container(
//           width: 300,
//           color: Colors.grey[200],
//           child: Column(
//             children: [
//               // Legend
//               Container(
//                 padding: EdgeInsets.all(8.0),
//                 color: Colors.blueGrey,
//                 child: Text(
//                   'Legend',
//                   style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold),
//                 ),
//               ),
//               // List of Node Categories
//               Expanded(
//                 child: ListView(
//                   children: [
//                     for (var builder in VSHelper.nodeBuilders)
//                       if (builder is VSSubgroup)
//                         ExpansionTile(
//                           title: Text(builder.name),
//                           children: [
//                             for (var block in builder.subgroup)
//                               ListTile(
//                                 title: Text(block.runtimeType.toString()),
//                                 onTap: () {
//                                   _addNode(); // Add node dynamically
//                                 },
//                               ),
//                           ],
//                         )
//                   ],
//                 ),
//               ),
//             ],
//           ),
//         ),

//         // Right Panel: Interactive Node View
//         Expanded(
//           child: Stack(
//             children: [
//               InteractiveVSNodeView(
//                 width: 5000,
//                 height: 5000,
//                 nodeDataProvider: nodeDataProvider,
//               ),
//               // Floating "Elevate" button
//               Positioned(
//                 bottom: 16,
//                 right: 16,
//                 child: FloatingActionButton(
//                   onPressed: () {
//                     // Logic to elevate or process nodes
//                   },
//                   child: Icon(Icons.arrow_upward),
//                 ),
//               ),
//             ],
//           ),
//         ),
//       ],
//     ),
//   );
// }

