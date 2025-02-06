import pandas as pd

class BasketballStatsAnalyzer:
    def __init__(self, file_path):
        """Loads the dataset from the provided file path and initializes the dataframe."""
        try:
            self.df = pd.read_csv(file_path)
        except FileNotFoundError:
            print("Error: File not found. Please provide a valid dataset path.")
        except pd.errors.EmptyDataError:
            print("Error: File is empty.")
        except pd.errors.ParserError:
            print("Error: File is not properly formatted.")
        
    def calculate_field_goal_accuracy(self):
        """Computes the field goal accuracy as FGM / FGA, handling division errors."""
        self.df['Field Goal Accuracy'] = self.df['FGM'] / self.df['FGA']
        self.df['Field Goal Accuracy'].fillna(0, inplace=True)
    
    def calculate_three_point_accuracy(self):
        """Computes the three-point shooting accuracy as 3PM / 3PA, handling division errors."""
        self.df['Three Point Accuracy'] = self.df['3PM'] / self.df['3PA']
        self.df['Three Point Accuracy'].fillna(0, inplace=True)
    
    def calculate_free_throw_accuracy(self):
        """Computes the free throw accuracy as FTM / FTA, handling division errors."""
        self.df['Free Throw Accuracy'] = self.df['FTM'] / self.df['FTA']
        self.df['Free Throw Accuracy'].fillna(0, inplace=True)
    
    def calculate_points_per_minute(self):
        """Computes the average points scored per minute as PTS / MIN, handling division errors."""
        self.df['Points Per Minute'] = self.df['PTS'] / self.df['MIN']
        self.df['Points Per Minute'].fillna(0, inplace=True)
    
    def calculate_overall_shooting_accuracy(self):
        """Computes overall shooting efficiency as (FGM + FTM) / (FGA + FTA), handling division errors."""
        self.df['Overall Shooting Accuracy'] = (self.df['FGM'] + self.df['FTM']) / (self.df['FGA'] + self.df['FTA'])
        self.df['Overall Shooting Accuracy'].fillna(0, inplace=True)
    
    def calculate_blocks_per_game(self):
        """Computes the average number of blocks per game as BLK / GP, handling division errors."""
        self.df['Blocks Per Game'] = self.df['BLK'] / self.df['GP']
        self.df['Blocks Per Game'].fillna(0, inplace=True)
    
    def calculate_steals_per_game(self):
        """Computes the average number of steals per game as STL / GP, handling division errors."""
        self.df['Steals Per Game'] = self.df['STL'] / self.df['GP']
        self.df['Steals Per Game'].fillna(0, inplace=True)
    
    def get_top_players(self, metric, top_n=100):
        """Retrieves the top n players based on the specified metric."""
        return self.df[['Season', 'Player', metric]].nlargest(top_n, metric)
    
    def export_results(self, output_path):
        """Saves the computed statistics to a CSV file for further analysis."""
        try:
            self.df.to_csv(output_path, index=False)
            print(f"Results successfully saved to {output_path}")
        except Exception as e:
            print(f"Error saving results: {e}")

# Usage example:
if __name__ == "__main__":
    file_path = "players_stats_by_season_full_details.csv"
    output_path = "basketball_analysis_results.csv"
    
    analyzer = BasketballStatsAnalyzer(file_path)
    analyzer.calculate_field_goal_accuracy()
    analyzer.calculate_three_point_accuracy()
    analyzer.calculate_free_throw_accuracy()
    analyzer.calculate_points_per_minute()
    analyzer.calculate_overall_shooting_accuracy()
    analyzer.calculate_blocks_per_game()
    analyzer.calculate_steals_per_game()
    analyzer.export_results(output_path)
