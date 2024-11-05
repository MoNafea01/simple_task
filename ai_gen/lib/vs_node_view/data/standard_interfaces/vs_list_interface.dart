import 'dart:async';

import 'package:ai_gen/vs_node_view/data/standard_interfaces/vs_num_interface.dart';
import 'package:ai_gen/vs_node_view/data/vs_interface.dart';
import 'package:flutter/material.dart';

const Color _interfaceColor = Colors.purple;

class VSListOutputData extends VSOutputData<List> {
  ///Basic List output interface
  VSListOutputData({
    required super.type,
    FutureOr<List<double>> Function(Map<String, dynamic>)? super.outputFunction,
  });

  @override
  Color get interfaceColor => _interfaceColor;
}

class VSListInputData extends VSInputData {
  ///Basic List input interface
  VSListInputData({
    required super.type,
    super.title,
    super.toolTip,
    super.initialConnection,
    super.interfaceIconBuilder,
  });

  @override
  List<Type> get acceptedTypes => [VSListOutputData, VSNumOutputData];

  @override
  Color get interfaceColor => _interfaceColor;
}
