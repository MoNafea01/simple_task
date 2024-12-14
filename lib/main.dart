import 'package:flutter/material.dart';

import 'block_view/example.dart';

void main() async {
  // print(await trainTestSplit([1, 2, 3, 4], testSize: 0.2, randomState: 1));
  runApp(const MyApp());
}

TextEditingController controller = TextEditingController();

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Test Demo',
      theme: ThemeData(
        scaffoldBackgroundColor: const Color.fromARGB(255, 46, 46, 46),
      ),
      home: const VSNodeExample(),
    );
  }
}
