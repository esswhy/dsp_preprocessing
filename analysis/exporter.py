import csv


class Exporter:
    @staticmethod
    def mean(x):
        # take a dict and return the mean of the values
        return [sum(x.values()) / len(x)]

    @staticmethod
    def all(x):
        # take a dict and return the values
        return list(map(str, x.values()))

    @staticmethod
    def export_efficiency_to_csv(efficiency, file_name, operation="mean"):
        header = "Header"
        if operation == "mean":
            operation = Exporter.mean
            header = ["ParticipantId",  "MeanEfficiency"]
        elif operation == "all":
            operation = Exporter.all
            header = ["ParticipantId"]
            efficiency_header = []
            for i in range(3, 23):
                efficiency_header.append(f"Efficiency {i}")
            header.extend(efficiency_header)

        with open(file_name, 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(header)

            for subject in efficiency.keys():
                row = [subject]
                row.extend(operation(efficiency[subject]))
                writer.writerow(row)

        print(f"Exported to {file_name}")

    @staticmethod
    def export_to_csv(angular_error, efficiency, file_name, operation="mean"):
        header = "Header"
        if operation == "mean":
            operation = Exporter.mean
            header = ["ParticipantId", "MeanAngularError", "MeanEfficiency"]
        elif operation == "all":
            operation = Exporter.all
            header = ["ParticipantId"]
            error_header = []
            efficiency_header = []
            for i in range(3, 23):
                error_header.append(f"Angular Error {i}")
                efficiency_header.append(f"Efficiency {i}")
            header.extend(error_header)
            header.extend(efficiency_header)

        with open(file_name, 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(header)

            # check if the length of the two dictionary are the same
            if len(angular_error) != len(efficiency):
                raise ValueError("The length of the two dictionary are not the same")

            for subject in angular_error.keys():
                row = [subject]
                row.extend(operation(angular_error[subject]))
                row.extend(operation(efficiency[subject]))
                writer.writerow(row)

        print(f"Exported to {file_name}")
