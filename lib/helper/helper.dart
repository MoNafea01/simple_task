class Helper {
  static List<double> parseList(String text) {
    return text
        .split(',') // Split the string by commas
        .map((e) => double.parse(e.trim())) // Parse each element to a double
        .toList();
  }
}
//list of inputs