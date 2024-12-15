// import 'package:ai_gen/vs_node_view/vs_node_view.dart';
// import 'package:flutter/gestures.dart';
// import 'package:flutter/material.dart';

// class InteractiveVSNodeView extends StatefulWidget {
//   ///Wraps [VSNodeView] in an [InteractiveViewer] this enables pan and zoom
//   ///
//   ///Creates a [SizedBox] of given width and height that will function as a canvas
//   ///
//   ///Width and height default to their coresponding screen dimension. If one of them is omited there will be no panning on that axis
//   const InteractiveVSNodeView({
//     super.key,
//     this.controller,
//     this.width,
//     this.height,
//     this.scaleFactor = kDefaultMouseScrollToScaleFactor,
//     this.maxScale = 2,
//     this.minScale = 0.01,
//     this.scaleEnabled = true,
//     this.panEnabled = true,
//     required this.nodeDataProvider,
//     this.baseNodeView,
//   });

//   ///TransformationController used by the [InteractiveViewer] widget
//   final TransformationController? controller;

//   ///The provider that will be used to controll the UI
//   final VSNodeDataProvider nodeDataProvider;

//   ///Width of the canvas
//   ///
//   ///Defaults to screen width
//   final double? width;

//   ///Height of the canvas
//   ///
//   ///Defaults to screen height
//   final double? height;

//   /// Determines the amount of scale to be performed per pointer scroll.
//   final double scaleFactor;

//   /// The maximum allowed scale.
//   final double maxScale;

//   /// The minimum allowed scale.
//   final double minScale;

//   /// If false, the user will be prevented from panning.
//   final bool panEnabled;

//   /// If false, the user will be prevented from scaling.
//   final bool scaleEnabled;

//   ///The [VSNodeView] that will be wrapped by the [InteractiveViewer]
//   final VSNodeView? baseNodeView;

//   @override
//   State<InteractiveVSNodeView> createState() => _InteractiveVSNodeViewState();
// }

// class _InteractiveVSNodeViewState extends State<InteractiveVSNodeView> {
//   late TransformationController controller;
//   late double width;
//   late double height;

//   @override
//   void initState() {
//     super.initState();
//     controller = widget.controller ?? TransformationController();
//   }

//   @override
//   Widget build(BuildContext context) {
//     final screenSize = MediaQuery.of(context).size;

//     width = widget.width ?? screenSize.width;
//     height = widget.height ?? screenSize.width;

//     //Needs to be done with a listener to assure inertia doesnt messup the offset
//     controller.addListener(
//       () {
//         widget.nodeDataProvider.viewportScale =
//             1 / controller.value.getMaxScaleOnAxis();

//         widget.nodeDataProvider.viewportOffset = Offset(
//           controller.value.getTranslation().x,
//           controller.value.getTranslation().y,
//         );
//       },
//     );

//     return InteractiveViewer(
//       maxScale: widget.maxScale,
//       minScale: widget.minScale,
//       scaleFactor: widget.scaleFactor,
//       scaleEnabled: widget.scaleEnabled,
//       panEnabled: widget.panEnabled,
//       constrained: false,
//       transformationController: controller,
//       child: SizedBox(
//         width: width,
//         height: height,
//         child: widget.baseNodeView ??
//             VSNodeView(
//               nodeDataProvider: widget.nodeDataProvider,
//             ),
//       ),
//     );
//   }
// }



// import 'package:ai_gen/vs_node_view/vs_node_view.dart';
// import 'package:flutter/gestures.dart';
// import 'package:flutter/material.dart';



import 'package:ai_gen/vs_node_view/data/vs_node_data_provider.dart';
import 'package:ai_gen/vs_node_view/widgets/vs_node_view.dart';
import 'package:flutter/gestures.dart';
import 'package:flutter/material.dart';

class InteractiveVSNodeView extends StatefulWidget {
  ///Wraps [VSNodeView] in an [InteractiveViewer] this enables pan and zoom
  ///
  ///Creates a [SizedBox] of given width and height that will function as a canvas
  ///
  ///Width and height default to their coresponding screen dimension. If one of them is omited there will be no panning on that axis
  const InteractiveVSNodeView({
    super.key,
    this.controller,
    this.width,
    this.height,
    this.scaleFactor = kDefaultMouseScrollToScaleFactor,
    this.maxScale = 2,
    this.minScale = 0.01,
    this.scaleEnabled = true,
    this.panEnabled = true,
    required this.nodeDataProvider,
    this.baseNodeView,
  });

  ///TransformationController used by the [InteractiveViewer] widget
  final TransformationController? controller;

  ///The provider that will be used to controll the UI
  final VSNodeDataProvider nodeDataProvider;

  ///Width of the canvas
  ///
  ///Defaults to screen width
  final double? width;

  ///Height of the canvas
  ///
  ///Defaults to screen height
  final double? height;

  /// Determines the amount of scale to be performed per pointer scroll.
  final double scaleFactor;

  /// The maximum allowed scale.
  final double maxScale;

  /// The minimum allowed scale.
  final double minScale;

  /// If false, the user will be prevented from panning.
  final bool panEnabled;

  /// If false, the user will be prevented from scaling.
  final bool scaleEnabled;

  ///The [VSNodeView] that will be wrapped by the [InteractiveViewer]
  final VSNodeView? baseNodeView;

  @override
  State<InteractiveVSNodeView> createState() => _InteractiveVSNodeViewState();
}

// class _InteractiveVSNodeViewState extends State<InteractiveVSNodeView> {
//   late TransformationController controller;
//   late double width;
//   late double height;

//   @override
//   void initState() {
//     super.initState();
//     controller = widget.controller ?? TransformationController();
//   }

//   @override
//   Widget build(BuildContext context) {
//     final screenSize = MediaQuery.of(context).size;

//     width = widget.width ?? screenSize.width;
//     height = widget.height ?? screenSize.height; // first update  width -------> height  [1]

//     //Needs to be done with a listener to assure inertia doesnt messup the offset
//     controller.addListener(
//       () {
//         widget.nodeDataProvider.viewportScale =
//             1 / controller.value.getMaxScaleOnAxis();

//         widget.nodeDataProvider.viewportOffset = Offset(
//           controller.value.getTranslation().x,
//           controller.value.getTranslation().y,
//         );
//       },
//     );

//     return InteractiveViewer(
//       maxScale: widget.maxScale,
//       minScale: widget.minScale,
//       scaleFactor: widget.scaleFactor,
//       scaleEnabled: widget.scaleEnabled,
//       panEnabled: widget.panEnabled,
//       constrained: false,
//       transformationController: controller,
//       child: Container(
//         color: Colors.grey[200],
//         child: SizedBox(
//           width: width,
//           height: height,
//           child: widget.baseNodeView ??
//               VSNodeView(
//                 nodeDataProvider: widget.nodeDataProvider,
//               ),
//         ),
//       ),
//     );
//   }
// }
 

 

class GridPainter extends CustomPainter {
  final double gridSpacing;
  final Color gridColor;

  GridPainter({this.gridSpacing = 20.0, this.gridColor = Colors.grey});

  @override
  void paint(Canvas canvas, Size size) {
    final paint = Paint()
      ..color = gridColor
      ..style = PaintingStyle.stroke;

    // Draw vertical lines
    for (double x = 0; x < size.width; x += gridSpacing) {
      canvas.drawLine(Offset(x, 0), Offset(x, size.height), paint);
    }

    // Draw horizontal lines
    for (double y = 0; y < size.height; y += gridSpacing) {
      canvas.drawLine(Offset(0, y), Offset(size.width, y), paint);
    }
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) {
    return false;
  }
}


class _InteractiveVSNodeViewState extends State<InteractiveVSNodeView> {
  late TransformationController controller;
  late double width;
  late double height;
  bool showGrid = false; // State variable to toggle grid visibility

  @override
  void initState() {
    super.initState();
    controller = widget.controller ?? TransformationController();
  }

  @override
  Widget build(BuildContext context) {
    final screenSize = MediaQuery.of(context).size;

    width = widget.width ?? screenSize.width;
    height = widget.height ?? screenSize.height;

    controller.addListener(
      () {
        widget.nodeDataProvider.viewportScale =
            1 / controller.value.getMaxScaleOnAxis();

        widget.nodeDataProvider.viewportOffset = Offset(
          controller.value.getTranslation().x,
          controller.value.getTranslation().y,
        );
      },
    );

//     return Stack(
//       children: [
//  if (showGrid) // Conditionally show the grid
//           CustomPaint(
//             size: Size(width, height),
//             painter: GridPainter(),
//           ),
//         Positioned(
//           top: 10,
//           right: 10,
//           child: Column(
//             children: [
//               ElevatedButton(
//                 onPressed: () {
//                   setState(() {
//                     showGrid = !showGrid; // Toggle grid visibility
//                   });
//                 },
//                 child: Text(showGrid ? "Hide Grid" : "Show Grid"),
//               ),
//             ],
//           ),
//         )
//         ,
//         InteractiveViewer(
//           maxScale: widget.maxScale,
//           minScale: widget.minScale,
//           scaleFactor: widget.scaleFactor,
//           scaleEnabled: widget.scaleEnabled,
//           panEnabled: widget.panEnabled,
//           constrained: false,
//           transformationController: controller,
//           child: SizedBox(
//             width: width,
//             height: height,
//             child: widget.baseNodeView ??
//                 VSNodeView(
//                   nodeDataProvider: widget.nodeDataProvider,
//                 ),
//           ),
//         ),
       
//       ],
//     );
return Stack(
  children: [
    Container(
        color: Colors.grey[900], // Light grey background
        width: width,
        height: height,
      ),
    // Draw the grid first, so it is behind the interactive viewer
    if (showGrid) 
      CustomPaint(
        size: Size(width, height),
        painter: GridPainter(),
      ),
    InteractiveViewer(
      maxScale: widget.maxScale,
      minScale: widget.minScale,
      scaleFactor: widget.scaleFactor,
      scaleEnabled: widget.scaleEnabled,
      panEnabled: widget.panEnabled,
      constrained: false,
      transformationController: controller,
      child: SizedBox(
        width: width,
        height: height,
        child: widget.baseNodeView ??
            VSNodeView(
              nodeDataProvider: widget.nodeDataProvider,
            ),
      ),
    ),
    Positioned(
      top: 10,
      right: 10,
      child: Column(
        children: [
          ElevatedButton(
            onPressed: () {
              setState(() {
                showGrid = !showGrid; // Toggle grid visibility
              });
            },
            child: Text(showGrid ? "Hide Grid" : "Show Grid"),
          ),
        ],
      ),
    ),
  ],
);
  }
}