class Helper {
  static List<double> parseList(String text) {
    return text
        .split(',') // Split the string by commas
        .map((e) => double.parse(e.trim())) // Parse each element to a double
        .toList();
  }
}
/*
class VSListOutputData extends VSOutputData<List> {
  ///Basic int output interface
  VSListOutputData({
    required String type,
    Future<List<double>> Function(Map<String, dynamic>)? outputFunction,
  }) : super(
    type: type,
    outputFunction:  outputFunction,
  );

  @override
  Color get interfaceColor => _interfaceColor;
}
class VSListInputData extends VSInputData {
  ///Basic int input interface
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
 */
