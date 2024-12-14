import 'dart:convert';

import 'package:http/http.dart' as http;

Future<Map<String, List<double>>> trainTestSplit(
  List<double> data, {
  double testSize = 0.2,
  int? randomState,
}) async {
  final url = Uri.parse('http://127.0.0.1:8000/ai/train-test-split/');

  final response = await http.post(
    url,
    headers: {'Content-Type': 'application/json'},
    body: jsonEncode({
      'data': data,
      'test_size': testSize,
      'random_state': randomState,
    }),
  );

  if (response.statusCode == 200) {
    final jsonResponse = jsonDecode(response.body);
    return {
      'X_train': List<double>.from(jsonResponse['X_train']),
      'X_test': List<double>.from(jsonResponse['X_test']),
    };
  } else {
    throw Exception('Failed to perform train-test split');
  }
}
