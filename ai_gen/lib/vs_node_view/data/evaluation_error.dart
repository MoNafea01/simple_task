import 'package:ai_gen/vs_node_view/vs_node_view.dart';

class EvalutationError {
  EvalutationError({
    required this.nodeData,
    required this.inputData,
    required this.error,
  });

  final VSNodeData nodeData;
  final Map<String, dynamic> inputData;

  final Object error;
}
