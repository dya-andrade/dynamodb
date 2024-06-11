package tech.buildrun.dynamodb.controller;

import io.awspring.cloud.dynamodb.DynamoDbTemplate;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import tech.buildrun.dynamodb.controller.dto.ScoreDto;
import tech.buildrun.dynamodb.entity.PlayerHistoryEntity;

@RestController
@RequestMapping("v1/players")
public class PlayerController {

    // interface que abstrai a comunicação com DynamoDB
    private final DynamoDbTemplate dynamoDbTemplate;

    public PlayerController(DynamoDbTemplate dynamoDbTemplate) {
        this.dynamoDbTemplate = dynamoDbTemplate;
    }

    @PostMapping("/{username}/games")
    public ResponseEntity<Void> save(@PathVariable("username") String username, @RequestBody ScoreDto scoreDto) {

        var entity = PlayerHistoryEntity.fromScore(username, scoreDto);

        dynamoDbTemplate.save(entity);

        return  ResponseEntity.ok().build();
    }
}
