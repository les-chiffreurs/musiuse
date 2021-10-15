import { StatusBar } from "expo-status-bar";
import React, { useState } from "react";
import { StyleSheet, Text, View, Button } from "react-native";
import { get_warning, Stwarn } from "./Scraper";

export default function App() {
  const [stwarn, setStwarn] = useState<Stwarn>({
    stations: new Array<string>(),
    warnings: new Array<string>(),
  });
  const [first, setFirst] = useState(true);
  if (first) {
    get_warning().then((stwarn) => {
      setStwarn(stwarn);
      setFirst(false);
    });
  }
  return (
    <View style={styles.container}>
      <View style={styles.allwarnings}>
        <View style={styles.stwarn}>
          {stwarn.stations.map((e, i) => (
            <Text key={e + i}>{e}</Text>
          ))}
        </View>
        <View style={styles.stwarn}>
          {stwarn.warnings.map((e, i) => (
            <Text key={e + i}>{e}</Text>
          ))}
        </View>
      </View>
      <Button
        title="refresh"
        onPress={() => {
          get_warning().then((stwarn) => {
            console.log("updating warnings");
            setStwarn(stwarn);
          });
        }}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
  },
  stwarn: {
    padding: 10,
  },
  allwarnings: {
    flexDirection: "row",
  },
});
