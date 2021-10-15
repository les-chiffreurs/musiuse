import axios from "axios";
import cheerio from "cheerio";

export type Stwarn = {
  stations: Array<string>;
  warnings: Array<string>;
};

export async function get_warning(): Promise<Stwarn> {
  const url = "https://zh.stwarn.ch/";

  const AxiosInstance = axios.create();
  let stations: Array<string> = new Array<string>();
  let warnings: Array<string> = new Array<string>();
  let response;
  try {
    response = await AxiosInstance.get(url);
  } catch (err) {
    console.log(err);
    console.log(`failed to get data from ${url}, please try again later`);
    return { stations: [], warnings: [] };
  }

  const html = response.data;
  const $ = cheerio.load(html);
  let station: string | null = null;
  $("td").each((i, e) => {
    if ($(e).text().endsWith("see")) {
      station = $(e).text();
      stations.push(station);
    } else if (station !== null) {
      warnings.push($(e).text());
      station = null;
    }
  });
  return { stations: stations, warnings: warnings };
}
